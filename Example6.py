usr_input = str(input("Enter a word or phrase: "))
str_len = len(usr_input)
usr_reverse = usr_input[str_len:0:-1]

if usr_input[0:str_len-1] == usr_reverse:
    print("Is a palindrome")
else:
    print("Not a palindrome")
