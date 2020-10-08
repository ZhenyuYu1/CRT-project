import random
runProgram = True
while(runProgram):
    user = input("Compost, Recycling, Trash.")
    choice = ["Compost", "Recycling", "Trash"]
    com = random.choice(choice)
    if (user == "Compost" and com == "Compost") or (user == "Recycling" and com == "Recyling") or (user == "Trash" and com == "Trash"):
        print("Tie.")
    elif (user == "Compost" and com == "Recycling") or (user == "Recycling" and com == "Trash") or (user == "Trash" and com == "Compost"):
        print("You win.")
    elif (user == "Compost" and com == "Trash") or (user == "Recycling" and com == "Compost") or (user == "Trash" and com == "Reycling"):
        print("You lose.")
    else:
        print("Please try again.")
        
    print(f'The computer chose: {com}')

    play = input("Play again?(Y/N)") 
    if play == "N":
        runProgram = False
    else:
        runProgram = True
print("The end.")