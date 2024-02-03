from dataclasses import dataclass
from os import getenv
from typing import Final

from dotenv import load_dotenv
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet

load_dotenv()
FILE: Final[str] = getenv("FILE_NAME", "den-sso.xlsx")
wb: Workbook = load_workbook(FILE)
sheets: list[str] = wb.sheetnames
ws: Worksheet = wb[sheets[0]]


@dataclass(slots=True)
class Coordinate:
    row: int
    column: int

    def _get_cell(self):
        return ws.cell(self.row, self.column)

    def _get_merged_cells_range(self):
        return [s for s in ws.merged_cells.ranges if self._get_cell().coordinate in s]

    def get_cell_value(self) -> str:
        """Get merged cell value"""
        range = self._get_merged_cells_range()
        result = (
            ws.cell(range[0].min_row, range[0].min_col).value
            if len(range) != 0
            else self._get_cell().value
        )
        return str(result) if result else ""

    def get_merged_cells(self) -> list["Coordinate"]:
        """Get merged cells"""
        range = self._get_merged_cells_range()
        return (
            [Coordinate(cell[0], cell[1]) for cell in range[0].bottom] if len(range) != 0 else []
        )


@dataclass(slots=True)
class Lesson:
    title: str
    cabinets: list[str]
    time: str
    number: int
    group_name: str


base_coordinate = Coordinate(26, 3)
time = Coordinate(base_coordinate.row, base_coordinate.column + 1).get_cell_value()


def parse_lesson(
    lesson_coordinate: Coordinate, time: str, number: int, header_distance: int
) -> Lesson:
    title = lesson_coordinate.get_cell_value()
    cabinets = parse_cabinets(
        Coordinate(
            lesson_coordinate.row,
            lesson_coordinate.column + len(lesson_coordinate.get_merged_cells()),
        ),
        header_distance,
    )
    group_name = Coordinate(
        lesson_coordinate.row - 1 - header_distance, lesson_coordinate.column
    ).get_cell_value()
    return Lesson(title=title, cabinets=cabinets, time=time, number=number, group_name=group_name)


def parse_cabinets_count(cabinets_coordinate: Coordinate, header_distance: int) -> int:
    return (
        len(
            Coordinate(
                cabinets_coordinate.row - 1 - header_distance,
                cabinets_coordinate.column,
            ).get_merged_cells()
        )
        or 1  # if cabinets column not merged
    )


def parse_cabinets(cabinets_coordinate: Coordinate, header_distance: int) -> list[str]:
    cabinets: list[str] = []
    for i in range(parse_cabinets_count(cabinets_coordinate, header_distance)):
        cabinet = Coordinate(
            cabinets_coordinate.row, cabinets_coordinate.column + i
        ).get_cell_value()
        if cabinet not in cabinets and cabinet != "":
            cabinets.append(cabinet)
    return cabinets


def parse_row(row_number_coordinate: Coordinate, header_distance: int) -> list[Lesson]:
    number = int(row_number_coordinate.get_cell_value())
    time = Coordinate(row_number_coordinate.row, row_number_coordinate.column + 1).get_cell_value()
    lessons = []
    lesson_coordinate = Coordinate(row_number_coordinate.row, row_number_coordinate.column + 2)
    while lesson_coordinate.get_cell_value() != "":
        lessons.append(parse_lesson(lesson_coordinate, time, number, header_distance))
        lesson_coordinate.column += parse_cabinets_count(
            Coordinate(lesson_coordinate.row, lesson_coordinate.column + 1),
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
