usr_list = []
usr_input = 0

print("======================================")
print("Input numbers to add to list. Will print out any numbers less than 5")
print("Exit the program by typing 'quit' or 'exit'")
print("======================================")

while True:
    usr_input = input("Enter the number: ")

    if usr_input == 'quit' or usr_input == 'exit':
        break
    elif usr_input.isdigit():                       # By default, all inputs are made str. Checks if input is an int digit. Won't work for negatives or floats.
        converted_input = int(usr_input)            # If str input is a digit, convert it to an int
        if converted_input < 5:
            usr_list.append(converted_input)        # Will only add to list if number is less than 5. More efficient than sorting it and picking


print("\n")
print(usr_list)
