import datetime

def parse_date(date_str):
    formats = ["%d %B %Y", "%Y-%m-%d", "%d %b %Y"]  # Add more formats as needed
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            pass
    return None