# meal.py

def main():
    # Prompt the user for the time in 24-hour format
    time = input("Enter the time (24-hour format): ").strip()

    # Convert the time to a float representing the number of hours
    hours = convert(time)

    # Determine and output the meal time
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    """
    This function converts time in 24-hour format (HH:MM) to the corresponding
    number of hours as a float.
    """
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
