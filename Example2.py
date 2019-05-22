import argparse

parser = argparse.ArgumentParser(description='Checks if numbers are even or odd. Can also see if two intergers are divisble.')
#Sets up description for what program does

"""
while(True):
    num = float(input("Type in a number: "))

    check = num % 2
    check_4 = num % 4
    if check == 0:
        print("It's even!")
        if check_4 == 0:
            print("And it's also divisible by 4!\n")
    else:
        print("It's not even\n")
"""

args = parser.parse_args()
