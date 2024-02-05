from dataclasses import dataclass

from vgpk_parser.coordinate import Coordinate
from vgpk_parser.row import Row, parse_row


@dataclass
class Section:
    rows: list[Row]
    end_row: int


def parse_section(section_coordinate: Coordinate) -> Section:
    rows: list[Row] = []
    start_row = section_coordinate.row
    while section_coordinate.get_cell_value().strip() != "":
        rows.append(
            parse_row(
                Coordinate(section_coordinate.row, 3),
                section_coordinate.row - start_row,
            )
        )
        section_coordinate.row += 1
    return Section(rows, section_coordinate.row - 1)
