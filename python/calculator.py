while True:
    operator = input("What is the operation you'd like to perform?")
    if operator == "done":
        print("Goodbye!")
        break
    first_number = int(input("What is the first number?"))
    second_number = int(input("What is the second number?"))

    add = (first_number + second_number)
    subtract = (first_number - second_number)
    divide = (first_number / second_number)
    multiply = (first_number * second_number)

    if operator == "add":
        print(first_number, "+", second_number, "=", first_number + second_number)
    elif operator == "subtract":
        print(first_number, "-", second_number, "=", first_number - second_number)
    elif operator == "divide":
        print(first_number, "/", second_number, "=", first_number / second_number)
    elif operator == "multiply":
        print(first_number, "*", second_number, "=", first_number * second_number)
    else:
        print("Invalid")
