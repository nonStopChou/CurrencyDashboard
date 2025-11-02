from datetime import datetime, date

def string_to_date(str_date: str) -> date:
    try:
        year, month, day = map(int, str_date.split("/"))
        return date(year, month, day)
    except Exception as error:
        print(f"can not parse the input string date {str_date}")
        return None


def time_alignment(time_input) -> datetime:
    if isinstance(time_input, datetime):
        aligned = time_input.replace(hour=0, minute=0, second=0, microsecond=0)
    elif isinstance(time_input, date):
        aligned = datetime.combine(time_input, datetime.min.time())
    elif isinstance(time_input, (int, float)):  # timestamp
        dt = datetime.fromtimestamp(time_input)
        aligned = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        raise TypeError(f"Unsupported type: {type(time_input)}")
    return aligned.timestamp()


def get_file_name(time_input):
    if isinstance(time_input, datetime):
        filename = time_input.strftime("%Y-%m-%d")
    elif isinstance(time_input, date):
        filename = time_input.strftime("%Y-%m-%d")
    elif isinstance(time_input, (int, float)):  # timestamp
        filename = datetime.fromtimestamp(time_input).strftime("%Y-%m-%d")
    else:
        raise TypeError(f"Unsupported type: {type(time_input)}")
    return f"{filename}.json"
