import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    return f"{datetime.fromisoformat(iso_string).strftime('%A%D%B%Y')}"


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    return(round((temp_in_fahrenheit - 32) * 5.0/9.0,1))


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = sum(weather_data)
    count = len(weather_data)
    mean =  total / count 
    return float(mean)

numbers = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
mean = calculate_mean(numbers)
print (mean)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                weather_data.append(row)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    info = [(value) for value in weather_data]
    min_value = min(info)
    min_index = len(info) -1 - info[::-1].index(min_value)
    return (min_value, min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    info = [(value) for value in weather_data]
    max_value = max(info)
    max_index = len(info) -1 - info[::-1].index(max_value)
    return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    info = [float(day[1]) for day in weather_data]
    min_temp, min_index = find_min(info) 
    max_temp, max_index = find_max(info)
    mean_temp = calculate_mean(info) 


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ""
    for day in weather_data:
        date = convert_date(day[0])
        min_temp = format_temperature(convert_f_to_c(float(day[1])))
        max_temp = format_temperature(convert_f_to_c(float(day[2])))
        daily_summary += f"---- {date} ----\n"
        daily_summarey += f"minimum temperature: {min_temp}\n"
        daily_summary += f"maximum temperature: {max_temp}\n\n"
        return daily_summary.strip()
    summary = (); generate_summary(weather_data)
    return summary