def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    """
    This function accepts a string formatted as $##.##, removes the leading $,
    and returns the amount as a float.
    """
    return float(d.strip('$'))

def percent_to_float(p):
    """
    This function accepts a string formatted as ##%, removes the trailing %,
    and returns the percentage as a float.
    """
    return float(p.strip('%')) / 100

main()
