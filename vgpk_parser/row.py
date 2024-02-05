from dataclasses import dataclass

from vgpk_parser.cabinets import parse_cabinets_count
from vgpk_parser.coordinate import Coordinate
from vgpk_parser.lesson import Lesson, parse_lesson


@dataclass
class Row:
    lessons: list[Lesson]
    time: str
    number: int


def parse_row(row_number_coordinate: Coordinate, header_distance: int) -> Row:
    lessons: list[Lesson] = []
    number = int(row_number_coordinate.get_cell_value())
    time = row_number_coordinate.copy(column_offset=1).get_cell_value()
    lesson_coordinate = row_number_coordinate.copy(column_offset=2)
    while lesson_coordinate.get_cell_value().strip() != "":
        lessons.append(parse_lesson(lesson_coordinate, header_distance))
        lesson_coordinate.column += parse_cabinets_count(
            lesson_coordinate.copy(column_offset=1),
            header_distance,
        ) + (len(lesson_coordinate.get_merged_cells()) or 1)
    return Row(lessons, time, number)
