import random

usr_input = None

while True:
    result = random.randint(1,9)
    counter = 0

    while usr_input != "exit":
        usr_input = input("Guess a number between 1 and 9: ")
        if usr_input.isdigit():
            converted_input = int(usr_input)

            if converted_input > result:
                print("That's too high!")
                counter += 1
            elif converted_input < result:
                print("That's too low!")
                counter += 1
            elif converted_input == result:
                print("Congrats! You guessed right!")
                print("And it took you "+ str(counter) + " tries to guess it!\n")
                counter += 1

                quit_command = str(input("Would you like to go again? Y/N: "))
                if quit_command == "Y" or quit_command == "y":
                    print("The game starts anew...\n")
                    break;
                if quit_command == "N" or quit_command == "n":
                    print("See ya!")
                    usr_input = "exit"

    if usr_input == "exit":
        break
