# ============================================================================
# Authors:            Artur Porebski (Aldec Inc.)
#
# Package installer:  Tools to extract data from UCIS datafiles.
#
# License:
# ============================================================================
# Copyright 2021 Aldec Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
# Aldec Revision:
# 10/10/21 - initial version
# 12/12/21 - additional switches: --units and --hierarchy
# End Aldec Revision
# ============================================================================
# usage: ucdb2cobertura.py [-h] -i INPUT -o OUTPUT [--units | --hierarchy]
#
# Arguments:
#  -h, --help            show this help message and exit
#  -i INPUT, --input INPUT
#                        Input UCDB XML file
#  -o OUTPUT, --output OUTPUT
#                        Output Cobertura XML file
#  --units               Statement coverage summary based on design units (default)
#  --hierarchy           Statement coverage summary based on hierarchy
# ============================================================================

from time import time
from lxml import etree
from collections import defaultdict, namedtuple
from itertools import groupby
from operator import attrgetter
from typing import List, Dict

StatementData = namedtuple(
    "StatementData",
    ["file", "line", "index", "instance", "hits"],
)


class CoberturaClass:
    def __init__(self, name: str, source_file: str):
        self.name: str = name
        self.source_file: str = source_file
        self.lines: Dict[int, int] = {}
        self.lines_valid: int = 0
        self.lines_covered: int = 0

    def add_statement(self, line: int, hits: int) -> None:
        assert line not in self.lines.keys(), "Duplicated line number"
        self.lines[line] = hits
        self.lines_valid += 1
        if hits:
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
        self.name: str = name
        self.classes: Dict[str, CoberturaClass] = {}
        self.lines_valid: int = 0
        self.lines_covered: int = 0

    def add_class(self, cobertura_class: CoberturaClass):
        assert cobertura_class.name not in self.classes, "Duplicated class name"
        self.classes[cobertura_class.name] = cobertura_class

    def update_statistics(self):
        for cobertura_class in self.classes.values():
            self.lines_covered += cobertura_class.lines_covered
            self.lines_valid += cobertura_class.lines_valid

    def get_xml_node(self) -> etree.Element:
        classes_node = etree.Element("classes")
        package_node = etree.Element("package")
        package_node.attrib["name"] = self.name
        package_node.attrib["complexity"] = "0"
        package_node.attrib["branch-rate"] = "0"
        package_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)

        package_node.append(classes_node)

        for cobertura_class in self.classes.values():
            classes_node.append(cobertura_class.get_xml_node())

        return package_node


class CoberturaCoverage:
    def __init__(self):
        self.sources: set = set()
        self.packages: Dict[str, CoberturaPackage] = {}
        self.lines_valid: int = 0
        self.lines_covered: int = 0

    def add_source(self, source: str):
        self.sources.add(source)

    def add_package(self, package: CoberturaPackage):
        assert package.name not in self.packages, "Duplicated package name"
        self.packages[package.name] = package

    def update_statistics(self):
        for package in self.packages.values():
            package.update_statistics()
            self.lines_covered += package.lines_covered
            self.lines_valid += package.lines_valid

    def get_xml(self) -> etree.Element:
        self.update_statistics()

        coverage_node = etree.Element("coverage")
        coverage_node.attrib["version"] = "5.5"
        coverage_node.attrib["timestamp"] = str(int(time()))
        coverage_node.attrib["branches-valid"] = "0"
        coverage_node.attrib["branches-covered"] = "0"
        coverage_node.attrib["branch-rate"] = "0"
        coverage_node.attrib["complexity"] = "0"

        sources_node = etree.Element("sources")

        for source in self.sources:
            etree.SubElement(sources_node, "source").text = source

        coverage_node.append(sources_node)

        packages_node = etree.Element("packages")

        for package in self.packages.values():
            packages_node.append(package.get_xml_node())

        coverage_node.append(packages_node)

        coverage_node.attrib["lines-valid"] = str(self.lines_valid)
        coverage_node.attrib["lines-covered"] = str(self.lines_covered)
        coverage_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)

        return etree.tostring(
            coverage_node, pretty_print=True, encoding="utf-8", xml_declaration=True
        )


class UcdbParser:
    def __init__(self, filename: str, merge_instances: bool):
        self.merge_instances = merge_instances

        file = open(filename)
        self.tree = etree.parse(filename)
        file.close()

        self.nsmap = self.tree.getroot().nsmap

        self.coverage = CoberturaCoverage()
        self.statements_count = 0
        self.statements_covered = 0

    def get_cobertura_model(self):
        self.parse_statement_coverage()

        return self.coverage

    def group_by_index(self, statements: List[StatementData]):
        grouped_stmts = []

        sorted_stmts = sorted(statements, key=attrgetter("index"))
        for index, stmts in groupby(sorted_stmts, key=attrgetter("index")):
            hit = any((stmt.hits for stmt in stmts))

            grouped_stmts.append(
                StatementData(
                    file=statements[0].file,
                    line=statements[0].line,
                    index=index,
                    instance="",
                    hits=hit,
                )
            )

        return grouped_stmts

    def parse_statement_coverage(self):
        scopes = self.tree.xpath(
            "/ux:ucdb/ux:scope[.//ux:bin[@type='STMTBIN']]", namespaces=self.nsmap
        )

        nodes = []

        for scope_node in scopes:
            if scope_node.get("type").startswith("DU_"):
                continue
            nodes.extend(
                scope_node.xpath(".//ux:bin[@type='STMTBIN']", namespaces=self.nsmap)
            )

        statements = defaultdict(lambda: defaultdict(list))

        for node in nodes:
            workdir, stmt_data = self.parse_statement_node(node)
            self.coverage.add_source(workdir)
            statements[stmt_data.file][stmt_data.line].append(stmt_data)

        for file, file_lines in statements.items():
            package = CoberturaPackage(file)
            cobertura_class = CoberturaClass(file, file)
            package.add_class(cobertura_class)
            self.coverage.add_package(package)

            for line, line_stmts in file_lines.items():
                if self.merge_instances:
                    line_stmts = self.group_by_index(line_stmts)

                self.statements_count += len(line_stmts)

                covered = len(list(filter(attrgetter("hits"), line_stmts)))
                hit = int(covered == len(line_stmts))

                self.statements_covered += covered

                cobertura_class.add_statement(line, hit)

    def parse_statement_node(self, node):
        src_node = node.find("./ux:src", namespaces=self.nsmap)
        workdir = src_node.get("workdir")

        instance_path = ".".join(
            (scope.get("name") for scope in node.iterancestors("{*}scope"))
        )

        stmt_index = int(
            node.find("./ux:attr[@key='#SINDEX#']", namespaces=self.nsmap).text
        )

        count = int(node.find("./ux:count", namespaces=self.nsmap).text)

        stmt_data = StatementData(
            file=src_node.get("file"),
            line=int(src_node.get("line")),
            index=stmt_index,
            instance=instance_path,
            hits=count,
        )

        return workdir, stmt_data


if __name__ == "__main__":
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input UCDB XML file",
    )

    arg_parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output Cobertura XML file",
    )

    group = arg_parser.add_mutually_exclusive_group()

    group.add_argument(
        "--units",
        action="store_const",
        dest="type",
        const="units",
        help="Statement coverage summary based on design units (default)",
    )

    group.add_argument(
        "--hierarchy",
        action="store_const",
        dest="type",
        const="hierarchy",
        help="Statement coverage summary based on hierarchy",
    )

    arg_parser.set_defaults(type="h")

    args = arg_parser.parse_args()

    parser = UcdbParser(
        args.input,
        args.type == "units",
    )

    model = parser.get_cobertura_model()

    with open(args.output, "w") as output_file:
        output_file.write(model.get_xml().decode("utf-8"))

    print("Covered {}% of lines".format(model.lines_covered / model.lines_valid * 100))

    print(
        "Covered {}% of statements".format(
            parser.statements_covered / parser.statements_count * 100
        )
    )
