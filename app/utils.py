from datetime import datetime

def parse_date(string_date):
    try:
        d = datetime.strptime(string_date, "%Y-%m-%d %H")
    except ValueError:
        d = datetime.strptime(string_date, "%Y-%m-%d")
    return d

def date_to_string(date):
     d = datetime.strftime(date, "%Y-%m-%d %H")
     return d