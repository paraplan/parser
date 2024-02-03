from dataclasses import dataclass

from vgpk_parser.cabinets import parse_cabinets
from vgpk_parser.coordinate import Coordinate


@dataclass(slots=True)
class Lesson:
    title: str
    cabinets: list[str]
    time: str
    number: int
    group_name: str


def parse_lesson(
    lesson_coordinate: Coordinate, time: str, number: int, header_distance: int
) -> Lesson:
    title: str = lesson_coordinate.get_cell_value()
    cabinets = parse_cabinets(
        lesson_coordinate.copy(column_offset=len(lesson_coordinate.get_merged_cells()) or 1),
        header_distance,
    )
    group_name: str = lesson_coordinate.copy(row_offset=-header_distance - 1).get_cell_value()
    return Lesson(title=title, cabinets=cabinets, time=time, number=number, group_name=group_name)
