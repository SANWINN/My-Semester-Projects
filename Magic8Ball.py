#Saniya Winn
#1/27/2024
#Magic 8 Ball

#Init
import random
import time
magic8ballList = ["YES!", "Um, yeah, duh!", "Absolutely!", "Of course!", "Certainly", "I'm afraid not.", "Never!", "Sorry, no...", "NO!", "Let's not be delusional, no.", "Possibly...", "Perchance...", "Maybe", "It's too hard to tell.", "Just come back later...I'm on my lunch break of uncertainty."]
#Function
def magicBall():
    print("Welcome! Enter a yes or no question, and I'll tell you your fortune.")
    while True:
            question = str(input("Please enter a yes or no question."))
            checkpoint = question.endswith("?")
            if checkpoint == False:
                print("Please enter an ACTUAL question please.")
            if checkpoint == True:
                print("Shaking...")
                time.sleep(2)
                print("Shaking...")
                time.sleep(2)
                print("Shaking...")
                time.sleep(2)
                print(random.choice(magic8ballList))
            play = input("Would you like to play again? Input Y or N.")
            if play == "N":
                print("Thank you for playing with the Magic 8 Ball!")
                break
#Main
magicBall()
