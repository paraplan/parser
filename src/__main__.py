if __name__ == "__main__":
    import orjson
    from src.study_day import StudyDay

    with open("schedule.json") as file:
        text = file.read()
    data: dict = orjson.loads(text)
    # remove second area from data
    data["areas"] = data.get("areas", None)[:1]  # TODO: fix this
    print(StudyDay(**data))
