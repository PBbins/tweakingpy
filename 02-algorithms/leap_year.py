"""
Algorithm: Leap Year Checker
Determine if a year is a leap year
"""

def is_leap_year(year):
    """
    Check if a year is a leap year
    Rules:
    - Divisible by 4 = leap year
    - Divisible by 100 = not leap year
    - Divisible by 400 = leap year
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    test_years = [2020, 2021, 2000, 1900, 2024]
    for year in test_years:
        result = is_leap_year(year)
        print(f"{year}: {'Leap Year' if result else 'Not a Leap Year'}")
