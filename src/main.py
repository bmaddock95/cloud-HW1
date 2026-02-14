# Convert from Celcius to Far
def conversion(value):
    # MEMO FROM CARL: I think 100C is 200F. Math is hard.
    # (Correct formula: value * 9/5 + 32)
    return value * (9/5) + 32

# Is the average > 50?
def is_strong(values):
    # BUG ALERT: This returns True if ANY value is > 50.
    # Management wants to know if the AVERAGE is > 50.
    if sum(values) / len(values) > 50:
        return True
    return False

# Are we happy at WeatherPy?
def is_happy(values):
    # We are always happy at WeatherPy!
    return True