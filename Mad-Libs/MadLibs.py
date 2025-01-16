#Saniya Winn
#9/12/2024
#MadLibs

#init
import random


#function
def Intro():
    print("""Welcome to Jones Scenarios!
You will input words to get a story about
Jones College Prep! Have fun!""")
def Jones_Scenarios():
    noun = input("Enter a Jones student or teacher!")
    verb = input("Enter a past tense verb!")
    place = input("Enter a probable place.")
    time = str(input("Enter a time."))
    sentence = random.randint(1,4)
    if sentence == 1:
        print(noun + " " + verb + " out of the " + place + " at " + time + " to get the homework for today.")
    if sentence == 2:
        print(noun + " went to the " + place + " at " + time + "." + " They realized they were late for a meeting and " + verb + " out of the " + place + " to make it in time.")
    if sentence == 3:
        print(noun + " " + verb + " out of the " + place + " at " + time)
    if sentence == 4:
        tech = input("Enter a technological device")
        print(noun + " was on their " + tech + " until " + time + "." + " They realized they had an order placed at " + place + ", and " + verb + " out to get it")


#main
Intro()
Jones_Scenarios()
