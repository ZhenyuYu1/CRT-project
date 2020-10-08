import random
runProgram = True
playerWins = 0
computerWins = 0
numGames = 0
while(runProgram):
    user = input("Compost, Recycling, Trash.")
    choice = ["Compost", "Recycling", "Trash"]
    com = random.choice(choice)
    if (user == "Compost" and com == "Compost") or (user == "Recycling" and com == "Recyling") or (user == "Trash" and com == "Trash"):
        print("Tie.")
        numGames += 1
    elif (user == "Compost" and com == "Recycling") or (user == "Recycling" and com == "Trash") or (user == "Trash" and com == "Compost"):
        print("You win.")
        playerWins += 1
        numGames += 1
    elif (user == "Compost" and com == "Trash") or (user == "Recycling" and com == "Compost") or (user == "Trash" and com == "Recycling"):
        print("You lose.")
        computerWins += 1
        numGames += 1
    else:
        print("Please try again.")
        
    print(f'The computer chose: {com}')
    print(f'Player score: {playerWins}, {playerWins/numGames * 100} win rate.')
    print(f'Computer score: {computerWins}, {computerWins/numGames * 100} win rate.')
    print(f'Number of games played: {numGames}')

    play = input("Play again?(Y/N)") 
    if play == "N":
        runProgram = False
    else:
        runProgram = True
print("The end.")