from os import getenv
from typing import Final

from dotenv import load_dotenv
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet

load_dotenv()
FILE: Final[str] = getenv("FILE_NAME", "den-sso.xlsx")
work_book: Final[Workbook] = load_workbook(FILE)
sheets: list[str] = work_book.sheetnames
work_sheet: Final[Worksheet] = work_book[sheets[0]]
