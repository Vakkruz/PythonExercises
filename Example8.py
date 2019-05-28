ext_cmd = None

while ext_cmd != "N":
    plr_1 = str(input("Player 1, cast your lot!: "))
    plr_2 = str(input("Player 2, cast your lot!: "))

    if (plr_1 == "paper" and plr_2 == "rock") or (plr_1 == "rock" and plr_2 == "scissors") or (plr_1 == "scissors" and plr_2 == "paper") :
        print("Paper 1 wins!")
    if (plr_2 == "paper" and plr_1 == "rock") or (plr_2 == "rock" and plr_1 == "scissors") or (plr_2 == "scissors" and plr_1 == "paper") :
        print("Paper 2 wins!")

    ext_cmd = str(input("Wanna go another round? Y/N:"))
    print("\n")
