print("Give two numbers, and they shall by divided.\n"
      "Enter 'q' to quit")

while True:
    first = input("\nEnter the first number: ")
    if first == 'q':
        break
    second = input("Enter the second number: ")
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)


print("\nGive two numbers to be added.\n"
      "Enter 'q' to quit")

while True:
    num1 = input("\nEnter the first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break
    try:
        total = int(num1) + int(num2)
    except ValueError:
        print("Please enter numbers to be added")
    else:
        print(total)
