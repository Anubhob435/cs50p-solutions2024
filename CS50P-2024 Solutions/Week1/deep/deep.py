# deep.py

def main():
    # Prompt the user for the answer to the Great Question of Life, the Universe, and Everything
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Check if the answer is 42 or a variant of forty-two
    if is_correct_answer(answer):
        print("Yes")
    else:
        print("No")

def is_correct_answer(answer):
    """
    This function checks if the provided answer is 42 or (case-insensitively) forty-two or forty two.
    """
    answer = answer.strip().lower()
    return answer == "42" or answer == "forty-two" or answer == "forty two"

if __name__ == "__main__":
    main()
