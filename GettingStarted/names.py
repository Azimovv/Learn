from GettingStarted.name_function import get_formatted_name

print("Enter q at any time to quit. ")
while True:
    first = input("\nEnter a first name: ")
    if first == 'q':
        break
    last = input("Enter a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: {}".format(formatted_name))