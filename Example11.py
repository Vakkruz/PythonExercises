usr_input = int(input("Enter a number: "))

def div_chkr(number):
    div = 0

    for i in range(2,number):
        if (number%i) == 0:
            div += 1

    if div != 0:
        return True
    else:
        return False

if div_chkr(usr_input):
    print("This number is not prime")
else:
    print("This number is a prime number")
