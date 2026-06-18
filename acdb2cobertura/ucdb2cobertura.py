# ============================================================================
# Authors:            Artur Porebski (Aldec Inc.)
#
# Package installer:  Tools to extract data from UCIS datafiles.
#
# License:
# ============================================================================
# Copyright 2026 Aldec Inc.
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
# 03/01/22 - added support for exclusion flags
# 16/06/26 - replaced XPath with event driven parser
# End Aldec Revision
# ============================================================================
# usage: ucdb2cobertura.py [-h] -i INPUT -o OUTPUT [--units | --hierarchy]
#
# Arguments:
#  -h, --help            Show this help message and exit
#  -i INPUT, --input INPUT
#                        Input UCDB XML file
#  -o OUTPUT, --output OUTPUT
#                        Output Cobertura XML file
#  --units               Statement coverage summary based on design units (default)
#  --hierarchy           Statement coverage summary based on hierarchy
# ============================================================================

from time import time

from collections import defaultdict
from dataclasses import dataclass
from functools import partial
from itertools import groupby
from lxml import etree
from operator import attrgetter
from typing import List, Dict
from warnings import warn

UCDB_EXCLUDE_PRAGMA = 0x00000020
UCDB_EXCLUDE_FILE = 0x00000040
UCDB_EXCLUDE_INST = 0x00000080
UCDB_EXCLUDE_AUTO = 0x00000100

UCDB_EXCLUDED = (
    UCDB_EXCLUDE_FILE | UCDB_EXCLUDE_PRAGMA | UCDB_EXCLUDE_INST | UCDB_EXCLUDE_AUTO
)

@dataclass
class StatementData:
    file = ""
    line = 0
    index = 0
    instance = ""
    hits = 0

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

        try:
            class_node.attrib["line-rate"] = str(self.lines_covered / self.lines_valid)
        except ZeroDivisionError:
            class_node.attrib["line-rate"] = "1"

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

        try:
            package_node.attrib["line-rate"] = str(
                self.lines_covered / self.lines_valid
            )
        except ZeroDivisionError:
            package_node.attrib["line-rate"] = "1"

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

        try:
            coverage_node.attrib["line-rate"] = str(
                self.lines_covered / self.lines_valid
            )
        except ZeroDivisionError:
            coverage_node.attrib["line-rate"] = "1"
            warn("The Input file does not contain any valid statement nodes.")

        return etree.tostring(
            coverage_node, pretty_print=True, encoding="utf-8", xml_declaration=True
        )


class UcdbParser:
    ATTR_TAG = None
    BIN_TAG = None
    COUNT_TAG = None
    SCOPE_TAG = None
    SRC_TAG = None

    def __init__(self, merge_instances: bool):
        self.merge_instances = merge_instances

        self.tag_start_handlers = {}
        self.tag_end_handlers = {}
        self.data_handler = None

        self.scope_stack = []

        self.current_statement_data = None
        self.current_instance_path_cached = None
        self.is_current_statement_excluded = False

        self.statements = defaultdict(lambda: defaultdict(list))

        self.coverage = CoberturaCoverage()
        self.statements_count = 0
        self.statements_covered = 0

    def close(self):
        pass

    def start_ns(self, prefix, uri):
        if prefix != "ux":
            return

        self.init_handlers(uri)

    def start(self, tag, attributes):
        if tag not in self.tag_start_handlers:
            return

        self.tag_start_handlers[tag](attributes)
    
    def end(self, tag):
        if tag not in self.tag_end_handlers:
            return

        self.tag_end_handlers[tag]()

    def data(self, text):
        if self.data_handler is None:
            return

        self.data_handler(text)
        self.data_handler = None

    def init_tag_names(self, ux_uri):
        self.ATTR_TAG = f"{{{ux_uri}}}attr"
        self.BIN_TAG = f"{{{ux_uri}}}bin"
        self.COUNT_TAG = f"{{{ux_uri}}}count"
        self.SCOPE_TAG = f"{{{ux_uri}}}scope"
        self.SRC_TAG = f"{{{ux_uri}}}src"

    def init_handlers(self, uri):
        self.init_tag_names(uri)

        self.tag_start_handlers = {
            self.ATTR_TAG: self.handle_attr_start,
            self.BIN_TAG: self.handle_bin_start,
            self.COUNT_TAG: self.handle_count_start,
            self.SCOPE_TAG: self.handle_scope_start,
            self.SRC_TAG: self.handle_src_start,
        }

        self.tag_end_handlers = {
            self.BIN_TAG: self.handle_bin_end,
            self.SCOPE_TAG: self.handle_scope_end,
        }

    def handle_attr_start(self, attributes):
        if self.current_statement_data is None:
            return

        if "key" not in attributes or attributes["key"] != "#SINDEX#":
            return

        def index_handler(data, statement_data):
            statement_data.index = int(data)

        self.data_handler = partial(index_handler, statement_data = self.current_statement_data)

    def handle_bin_start(self, attributes):
        if not self.scope_stack or self.scope_stack[-1] is None:
            return

        if attributes.get("type", None) != "STMTBIN":
            return

        self.current_statement_data = StatementData()
        self.current_statement_data.instance = self.current_instance_path()
        self.is_current_statement_excluded = (int(attributes["flags"], 16) & UCDB_EXCLUDED) != 0

    def handle_bin_end(self):
        if self.current_statement_data is None:
            return

        statement_list = self.statements[self.current_statement_data.file]

        if not self.is_current_statement_excluded:
            statement_list[self.current_statement_data.line].append(self.current_statement_data)

        self.current_statement_data = None
        self.is_current_statement_excluded = False

    def handle_count_start(self, attributes):
        if self.current_statement_data is None:
            return

        def hits_handler(data, statement_data):
            statement_data.hits = int(data)

        self.data_handler = partial(hits_handler, statement_data = self.current_statement_data)

    def handle_scope_start(self, attributes):
        self.current_instance_path_cached = None

        if "type" in attributes and attributes["type"].startswith("DU_"):
            self.scope_stack.append(None)

            return

        if self.scope_stack and self.scope_stack[-1] is None:
            self.scope_stack.append(None)

            return

        self.scope_stack.append(attributes["name"])

    def handle_scope_end(self):
        self.current_instance_path_cached = None
        self.scope_stack.pop()

    def handle_src_start(self, attributes):
        if self.current_statement_data is None:
            return

        self.coverage.add_source(attributes["workdir"])

        self.current_statement_data.file = attributes["file"]
        self.current_statement_data.line = int(attributes["line"])

    def current_instance_path(self):
        if self.current_instance_path_cached is None:
            self.current_instance_path_cached = ".".join(self.scope_stack)

        return self.current_instance_path_cached

    def get_cobertura_model(self):
        self.convert_statement_coverage()

        return self.coverage

    def group_by_index(self, statements: List[StatementData]):
        grouped_stmts = []

        sorted_stmts = sorted(statements, key=attrgetter("index"))

        for index, stmts in groupby(sorted_stmts, key=attrgetter("index")):
            statement_data = StatementData()

            statement_data.file = statements[0].file
            statement_data.line = statements[0].line
            statement_data.index = index
            statement_data.hits = any((stmt.hits for stmt in stmts))

            grouped_stmts.append(statement_data)

        return grouped_stmts

    def convert_statement_coverage(self):
        for file, file_lines in self.statements.items():
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

    ucdb_parser = UcdbParser(args.type == "units")

    with open(args.input, "r") as file:
        etree.parse(file, etree.XMLParser(target=ucdb_parser))

    model = ucdb_parser.get_cobertura_model()

    with open(args.output, "w") as output_file:
        output_file.write(model.get_xml().decode("utf-8"))

    try:
        lines_coverage = model.lines_covered / model.lines_valid * 100
    except ZeroDivisionError:
        lines_coverage = 100

    print("Covered {}% of lines".format(lines_coverage))

    try:
        statement_coverage = ucdb_parser.statements_covered / ucdb_parser.statements_count * 100
    except ZeroDivisionError:
        statement_coverage = 100

    print("Covered {}% of statements".format(statement_coverage))
