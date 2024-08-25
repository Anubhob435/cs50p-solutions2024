def main():
    # Prompt the user for a greeting
    greeting = input("Enter your greeting: ").strip().lower()

    # Determine the appropriate amount based on the greeting
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
