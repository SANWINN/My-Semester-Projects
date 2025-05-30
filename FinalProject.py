#Saniya Winn
#Final Project

def Intro():
    print("""Annushka's (Anna) 18th birthday is fast approaching.
In her family, the 18th birthday is very important. Her family
sets up a scavenger hunt for her, hiding gold jewelry around their estate.
Her family tells her they hid 5 pieces of gold, and if she finds at least 3,
she can keep them all. Help Annushka find all 5 pieces.""")


def CodeAnnushka():
    while True:
        print("""Anna's mother tells her that one piece is in the backyard.
Anna sees 2 holes in the garden. She can only choose one.""")
        gold = 0
        choice1 = input("Should Anna go to the left or right hole?")

        if choice1 == "left":
            gold = gold + 1
            print("Anna found a piece of gold.")
            print("Anna now has " + str(gold) + " gold.")
        if choice1 == "right":
            gold = gold
            print("No gold for Anna.")
            print("Anna now has " + str(gold) + " gold.")

        print("""Anna's father tells her that one piece
of gold is in the family heirloom room. He tells her it
sticks out among the others. Anna goes into the room and
sees three pieces of gold jewelry. One is a gold necklace
with an amethyst pendant, one is a gold ring with amethyst gem,
and one is a gold ring with a sapphire gem.""")
        choice2 = input("""Should she pick the necklace (n),
amethyst ring (ar), or sapphire ring (sr)?""")

        if choice2 == "n":
            gold = gold
            print("No gold for Anna.")
            print("Anna now has " + str(gold) + " gold.")
        if choice2 == "ar":
            gold = gold
            print("No gold for Anna.")
            print("Anna now has " + str(gold) + " gold.")
        if choice2 == "sr":
            gold = gold + 1
            print("Anna found a piece of gold.")
            print("Anna now has " + str(gold) + " gold.")

        print("""Anna's family gives her no more hints.
She has to look herself. There's a 4-code safe, which has
to be the year her mother was born. She knows today is July 2025,
and her mother was born on June 12, and is 53.""")
        choice3 = input("What is the 4-digit code?")

        if choice3 == "1972":
            gold = gold + 1
            print("Anna found a piece of gold.")
            print("Anna now has " + str(gold) + " gold.")
        else:
            gold = gold
            print("No gold for Anna.")
            print("Anna now has " + str(gold) + """ gold, and her mother is very angry
because she didn't know her birth year.""")

        print("""Anna only has two more hunts left. She can now decide between
the barn (b), the garage (g), and the kitchen (k).""")
        choice4 = input("Where should Anna go? (Choose b, g, or k)")

        if choice4 == "b":
            print("""Anna goes into the barn only to see her horse
Dusk aggressively eating an apple. One more hunt left.""")
            gold = gold
            print("No gold for Anna.")
            print("Anna now has " + str(gold) + " gold.")
            choice5 = input("Should Anna go to the garage (g) or the kitchen (k)?")
            if choice5 == "g":
                print("Anna find a piece of gold in her mother's car.")
                gold = gold + 1
                print("Anna found a piece of gold.")
                print("Anna now has " + str(gold) + " gold.")
            if choice5 == "k":
                gold = gold + 1
                print("Anna found a piece of gold.")
                print("Anna now has " + str(gold) + " gold.")
        if choice4 == "g":
            print("Anna find a piece of gold in her mother's car.")
            gold = gold + 1
            print("Anna found a piece of gold.")
            print("Anna now has " + str(gold) + " gold.")
            choice5 = input("Should Anna go to the barn (b) or the kitchen (k)?")
            if choice5 == "k":
                gold = gold + 1
                print("Anna found a piece of gold.")
                print("Anna now has " + str(gold) + " gold.")
            if choice5 == "b":
                print("""Anna goes into the barn only to see her horse
Dusk aggressively eating an apple. One more hunt left.""")
                gold = gold
                print("No gold for Anna.")
                print("Anna now has " + str(gold) + " gold.")
        if choice4 == "k":
            gold = gold + 1
            print("Anna found a piece of gold.")
            print("Anna now has " + str(gold) + " gold.")
            choice5 = input("Should Anna go to the barn (b) or the garage (g)?")

            if choice5 == "b":
                print("""Anna goes into the barn only to see her horse
Dusk aggressively eating an apple. One more hunt left.""")
                gold = gold
                print("No gold for Anna.")
                print("Anna now has " + str(gold) + " gold.")
            if choice5 == "g":
                print("Anna find a piece of gold in her mother's car.")
                gold = gold + 1
                print("Anna found a piece of gold.")
                print("Anna now has " + str(gold) + " gold.")

        lap = input("Would you like to play again?")
        if lap == "yes":
            CodeAnnushka()
        elif lap == "no":
            break



#main
Intro()
CodeAnnushka()



