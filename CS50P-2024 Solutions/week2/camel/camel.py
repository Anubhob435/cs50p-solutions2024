def camel_to_snake(name):
    snake_case = ""

    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    return snake_case

def main():
    camel_case_name = input("camelCase: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("snakeCase:" + snake_case_name)

if __name__ == "__main__":
    main()
