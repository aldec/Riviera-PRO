# (c) Aldec, Inc.
# All rights reserved.
#
# Version: 1.01
# File: ucdb2cobertura.py
#
# Usage:
# acdb2xml -i aggregate.acdb -o ucdb.xml
# python ucdb2cobertura.py -i ucdb.xml -o cobertura.xml

 

from time import time
from lxml import etree


class CoberturaClass:
    def __init__(self, source_file: str):
        self.source_file = source_file  # type: str
        self.lines = {}  # type: dict[int, int]
        self.lines_valid = 0  # type: int
        self.lines_covered = 0  # type: int

    def add_statement(self, line: int, count: int) -> None:
        assert line not in self.lines.keys()
        self.lines[line] = count
        self.lines_valid += 1
        if count:
            self.lines_covered += 1

    def get_xml_node(self) -> etree.Element:
        class_node = etree.Element("class")
        class_node.attrib["name"] = self.source_file
        class_node.attrib["filename"] = self.source_file
        class_node.attrib["complexity"] = "0"
        class_node.attrib["branch-rate"] = "0"
        class_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)
        class_node.append(etree.Element("methods"))
        lines_node = etree.SubElement(class_node, "lines")

        for line in self.lines:
            etree.SubElement(
                lines_node,
                "line",
                number=str(line),
                hits=str(self.lines[line]),
            )

        return class_node


class CoberturaPackage:
    def __init__(self, name: str):
        self.name = name  # type: str
        self.classes = {}  # type: dict[str, CoberturaClass]
        self.lines_valid = 0  # type: int
        self.lines_covered = 0  # type: int

    def add_statement(self, class_name: str, source_file: str, line: int, count: int) -> None:
        try:
            self.classes[class_name].add_statement(line, count)
        except KeyError:
            self.classes[class_name] = CoberturaClass(source_file)
            self.classes.get(class_name).add_statement(line, count)

        self.lines_valid += 1

        if count:
            self.lines_covered += 1

    def get_xml_node(self) -> etree.Element:
        classes_node = etree.Element("classes")
        package_node = etree.Element("package")
        package_node.append(classes_node)
        package_node.attrib["name"] = self.name
        package_node.attrib["complexity"] = "0"
        package_node.attrib["branch-rate"] = "0"
        package_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)

        for (class_name, class_data) in self.classes.items():
            classes_node.append(class_data.get_xml_node())

        return package_node


class CoberturaCoverage:
    def __init__(self):
        self.sources = set()  # type: set
        self.packages = {}  # type: dict[str, CoberturaPackage]
        self.lines_valid = 0  # type: int
        self.lines_covered = 0  # type: int

    def add_statement(self, source: str, file: str, line: int, count: int) -> None:
        try:
            self.packages[source].add_statement(file, file, line, count)
        except KeyError:
            self.packages[source] = CoberturaPackage(file)
            self.packages.get(source).add_statement(file, file, line, count)

        self.sources.add(source)

        self.lines_valid += 1

        if count:
            self.lines_covered += 1

    def add_branch(self) -> None:
        pass

    def get_xml(self) -> etree.Element:
        coverage_node = etree.Element("coverage")
        coverage_node.attrib["version"] = "5.5"
        coverage_node.attrib["timestamp"] = str(int(time()))
        coverage_node.attrib["branches-valid"] = "0"
        coverage_node.attrib["branches-covered"] = "0"
        coverage_node.attrib["branch-rate"] = "0"
        coverage_node.attrib["complexity"] = "0"
        coverage_node.attrib["lines-valid"] = str(self.lines_valid)
        coverage_node.attrib["lines-covered"] = str(self.lines_covered)
        coverage_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)

        sources_node = etree.Element("sources")

        for source in self.sources:
            etree.SubElement(sources_node, "source").text = source

        coverage_node.append(sources_node)

        packages_node = etree.Element("packages")

        for package_name in self.packages:
            packages_node.append(self.packages[package_name].get_xml_node())

        coverage_node.append(packages_node)

        return etree.tostring(coverage_node, pretty_print=True, encoding="utf-8", xml_declaration=True)


class UcdbParser:
    def __init__(self, filename):
        file = open(filename)
        self.tree = etree.parse(filename)
        file.close()

        self.nsmap = self.tree.getroot().nsmap

        self.coverage = CoberturaCoverage()

    def get_cobertura_model(self):
        self.parse_statement_coverage()

        return self.coverage

    def parse_statement_coverage(self):
        nodes = self.tree.xpath("//ux:bin[@type='STMTBIN']", namespaces=self.nsmap)
        for node in nodes:
            self.parse_statement_node(node)

    def parse_statement_node(self, node):
        count = int(node.find("./ux:count", namespaces=self.nsmap).text)
        src_node = node.find("./ux:src", namespaces=self.nsmap)
        file_name = src_node.get("file")
        source = src_node.get("workdir")
        line = int(src_node.get("line"))

        self.coverage.add_statement(source, file_name, line, count)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input UCDB XML file")
    parser.add_argument("-o", "--output", help="Output Cobertura XML file")

    args = parser.parse_args()

    parser = UcdbParser(args.input)
    model = parser.get_cobertura_model()

    with open(args.output, 'w') as output_file:
        output_file.write(model.get_xml().decode("utf-8"))

    print("Covered {}% of statements".format(model.lines_covered / model.lines_valid * 100))
