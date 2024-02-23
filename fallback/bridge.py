from datetime import time

import orjson

from fallback.models import FallbackBells
from vgpk_parser.bells import Bells


def generate_fallback():
    with open("bells.json") as file:
        data = file.read()
    bells = Bells(**orjson.loads(data))
    print(fallback_bells(bells))


def fallback_bells(bells: Bells) -> FallbackBells:
    bells_title = {0: "Zero", 1: "First", 3: "Second", 5: "Third", 7: "Fourth", 9: "Fifth"}
    i: int = 0
    result_bells: dict[str, list[str]] = dict()
    while i < 10:
        bells_str = [fallback_bell_to_str(bells.hours[i].start, bells.hours[i].end)]
        if i != 0:
            bells_str.append(
                fallback_bell_to_str(bells.hours[i + 1].start, bells.hours[i + 1].end)
            )
        result_bells.update({bells_title[i]: bells_str})
        if i == 0:
            i += 1
        else:
            i += 2
    return FallbackBells(**result_bells)


def fallback_bell_to_str(start_hour: time, end_hour: time) -> str:
    pattern: str = "%H.%M"
    return " – ".join((start_hour.strftime(pattern), end_hour.strftime(pattern)))
