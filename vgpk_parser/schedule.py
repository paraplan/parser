from dataclasses import dataclass
from datetime import date

from vgpk_parser.client import START_COLUMN, START_ROW, work_sheet
from vgpk_parser.coordinate import Coordinate
from vgpk_parser.section import Section, parse_section


@dataclass
class Schedule:
    sections: list[Section]
    date: date


def parse_schedule() -> Schedule:
    sections: list[Section] = []
    base_coordinate = Coordinate(START_ROW, START_COLUMN)
    while base_coordinate.get_cell_value().strip() != "":
        section = parse_section(base_coordinate)
        sections.append(section)
        base_coordinate.row = section.end_row + 3
    return Schedule(sections, date(2024, *map(int, work_sheet.title.split("."))))
