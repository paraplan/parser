if __name__ == "__main__":
    import orjson

    from src.models.study_day import StudyDay

    with open("schedule.json") as file:
        text = file.read()
    data: dict = orjson.loads(text)
    print(StudyDay(**data))
