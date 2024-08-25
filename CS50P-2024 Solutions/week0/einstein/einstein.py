# einstein.py

def main():
    """
    This function prompts the user for mass in kilograms, calculates the energy
    equivalent in Joules using the formula E = mc^2, and prints the result.
    """
    # Prompt the user for mass as an integer
    mass = int(input())

    # Speed of light in meters per second
    c = 300_000_000  # 300,000,000

    # Calculate the energy using the formula E = mc^2
    energy = mass * (c ** 2)

    # Print the energy in Joules
    print(energy)

if __name__ == "__main__":
    main()
