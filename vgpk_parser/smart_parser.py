from vgpk_parser.cabinets import parse_cabinets_count
from vgpk_parser.coordinate import Coordinate
from vgpk_parser.lesson import Lesson, parse_lesson


def parse_row(row_number_coordinate: Coordinate, header_distance: int) -> list[Lesson]:
    number = int(row_number_coordinate.get_cell_value())
    time = row_number_coordinate.copy(column_offset=1).get_cell_value()
    lessons = []
    lesson_coordinate = row_number_coordinate.copy(column_offset=2)
    while lesson_coordinate.get_cell_value() != "":
        lessons.append(parse_lesson(lesson_coordinate, time, number, header_distance))
        lesson_coordinate.column += parse_cabinets_count(
            lesson_coordinate.copy(column_offset=1),
            header_distance,
        ) + (len(lesson_coordinate.get_merged_cells()) or 1)
    return lessons


def parse_section(section_start_coordinate: Coordinate) -> list[list[Lesson]]:
    rows: list[list[Lesson]] = []
    start_row = section_start_coordinate.row
    while len(section_start_coordinate.get_merged_cells()) < 10:
        rows.append(
            parse_row(
                Coordinate(section_start_coordinate.row, 3),
                section_start_coordinate.row - start_row,
            )
        )
        section_start_coordinate.row += 1
    return rows
