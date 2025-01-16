#Saniya Winn
#Period 5

#function
def gaming():
    print("Rock, Paper, Scissor ...")
    global player
    global computer
    player = input("Choose: Rock, Paper, or Scissors! ")
    print("Shoot!")
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "Rock"
    if computer == 2:
        computer = "Paper"
    if computer == 3:
        computer = "Scissors"
    print("Player chose: " + player)
    print("Computer chose: " + computer)
    check()

def check():
    global Pscore
    global Cscore
    global ties
    Pscore = 0
    Cscore = 0
    ties = 0
    if player == computer:
        print("Tie!")
        ties = ties + 1
    elif player.lower == "paper" and computer == "Rock":
        print("You win!")
        Pscore = Pscore + 1
    elif player.lower == "paper" and computer == "Scissors":
        print("You lose!")
        Cscore = Cscore + 1
    elif player.lower == "scissors" and computer == "Rock":
        print("You lose!")
        Cscore = Cscore + 1
    elif player.lower == "scissors" and computer == "Paper":
        print("You win!")
        Pscore = Pscore + 1
    elif player.lower == "rock" and computer == "Paper":
        print("You lose!")
        Cscore = Cscore + 1
    elif player.lower == "rock" and computer == "Scissors":
        print("You win!")
        Pscore = Pscore + 1
    else:
        print("Invalid argument!")
    print("Player: " + str(Pscore) + " / Computer: " + str(Cscore) + " / Ties: " + str(ties))

# main
print("Welcome to Rock, Paper, Scissors!")
gaming()
while True:
    option = input("Would you like to play again? ")
    if option.lower == "no":
        break
    else:
        gaming()
