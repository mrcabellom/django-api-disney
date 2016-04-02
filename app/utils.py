from datetime import datetime

def parse_date(string_date):
    try:
        d = datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        d = datetime.strptime(string_date, "%Y-%m-%d")
    return d

