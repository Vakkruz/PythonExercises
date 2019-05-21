usr_input = int(input("Enter a number: "))

for i in range(1,usr_input+1):
    if (usr_input%i) == 0:
        print(i)
