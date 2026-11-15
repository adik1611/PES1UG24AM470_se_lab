def _is_ascii_digits(s):
    """True only for a non-empty string of the plain digits 0-9.
    (str.isdigit() alone also accepts characters like '²' that int() rejects.)"""
    return isinstance(s, str) and s != "" and s.isascii() and s.isdigit()


def parse_ride_duration(text):
    """
    Converts a ride duration written as HH:MM into minutes.
    Returns None if the input is not a valid HH:MM string
    (not a string, missing/extra colons, non-digit parts, or minutes > 59).
    """
    if not isinstance(text, str):
        return None
    parts = text.strip().split(':')
    if len(parts) != 2:
        return None
    hours, minutes = parts[0].strip(), parts[1].strip()
    if not (_is_ascii_digits(hours) and _is_ascii_digits(minutes)):
        return None
    hours, minutes = int(hours), int(minutes)
    if minutes > 59:
        return None
    return hours * 60 + minutes

def format_station_code(code):
    """
    Formats a station code as ZONE-NUMBER, e.g. 'a12' -> 'A-12'.
    Returns None if the input is not a string made of one zone letter
    followed by one or more digits.
    """
    if not isinstance(code, str):
        return None
    code = code.strip().upper()
    if len(code) < 2:
        return None
    zone, number = code[0], code[1:]
    if not ('A' <= zone <= 'Z') or not _is_ascii_digits(number):
        return None
    return zone + '-' + number

def parse_ride_log(line):
    """
    Parses 'bike_type,minutes,subscriber' into a tuple.
    Returns None if the input is not a string with exactly three fields,
    a non-empty bike type and a non-negative integer number of minutes.
    """
    if not isinstance(line, str):
        return None
    parts = line.split(',')
    if len(parts) != 3:
        return None
    bike_type, minutes, subscriber = (p.strip() for p in parts)
    if bike_type == "" or not _is_ascii_digits(minutes):
        return None
    return bike_type, int(minutes), subscriber.lower() == 'yes'

def main():
    print("==== Running parse_ride_duration ====")
    value = input("Enter a ride duration as HH:MM (e.g. 01:15): ")
    result = parse_ride_duration(value)
    print("Duration in minutes:", result if result is not None else "Invalid input")

    print("\n==== Running format_station_code ====")
    value = input("Enter a station code (e.g. a12): ")
    result = format_station_code(value)
    print("Formatted station code:", result if result is not None else "Invalid input")

    print("\n==== Running parse_ride_log ====")
    value = input("Enter a ride log line as type,minutes,subscriber (e.g. electric,45,yes): ")
    result = parse_ride_log(value)
    print("Parsed ride log:", result if result is not None else "Invalid input")

if __name__ == "__main__":
    main()
