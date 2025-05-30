#init
Princesses = ["Tiana", "Aurora", "Snow White", "Mulan", "Pocahontas", "Jasmine", "Rapunzel", "Belle", "Ariel", "Cinderella", "Merida", "Moana", "Raya"]
Prices = [275,225,125,175,125,250,275,225,275,200,150,250,200]
Colors = ["green and brown", "light pink and blue", "blue and red and yellow", "red and black and dark blue",
          "teal and brown", "teal and yellow", "purple and yellow", "yellow and red", "purple and green",
          "light blue and yellow", "teal and orange", "orange and blue", "green and black"]
filteredList = []
filteredList2 = []
import random

#functions
def roomAvailable():
    while True:
        stay = random.randint(0,4)
        if stay == 0:
            print("Sorry, none of these princess rooms are available.")
            break
        else:
            print(str(stay)+" room(s) are available. Please check out to confirm your stay.\nThe program will reroute you to the main menu where one of the options is to check out.")
            break
def byPrincess():
    while True:
        print("The options are: \n1. Tiana \n2. Aurora \n3. Snow White \n4. Mulan \n5. Pocahantas \n6. Jasmine \n7. Rapunzel \n8. Belle \n9. Ariel \n10. Cinderella \n11. Merida \n12. Moana")
        room = int(input("Please input the number of the room you would like to learn more about:"))
        room = room - 1
        print(str(Princesses[room])+"'s room is "+str(Colors[room])+"! It costs $"+str(Prices[room])+" a night.")
        book = input("Would you like to book this room (y or n)?")
        if book == "y":
            roomAvailable()
            break
        if book == "n":
            break

def byColor(color):
    while True:
        for i in range(len(Colors)):
            if color in Colors[i]:
                filteredList.append(Colors[i])
        if filteredList != []:
            print("Here are your color combination options with this color: "+str(filteredList))
        else:
            print("Sorry, no rooms have this color. Your color combination options are: "+str(Colors))
        combo = input("Which color combiation would you like to learn more about?")
        number = Colors.index(combo)
        print("This is "+str(Princesses[number])+"'s room! It costs $"+str(Prices[number])+" a night.")
        book = input("Would you like to book this room (y or n)?")
        if book == "y":
            roomAvailable()
            break
        if book == "n":
            break
def byPrice():
    price = input("What is your budget for your stay? (no $)")
    for i in range(len(Prices)):
        if str(price) >= str(Prices[i]):
            filteredList2.append(Princesses[i])
    if filteredList2 != []:
        input("Here are the rooms that are within your budget: " + str(filteredList2) + ". Which princess room would you like to stay in?")
        print("The price for this room is $"+str(Prices[i])+" and this room is decorated with the colors "+Colors[i])
        roomAvailable()
    else:
        print("Sorry, there are no rooms within this budget.")

def PrincessPalaceMenu():
    print("Welcome to the Princess Palace Hotel Program!\nHere, you can filter your preferred room by color, favorite princess, and by price.")
    while True:
        choice = input("What would you like to select a room by? Price (p), princess (pr), or color (c)? \nOr, if you are done using the Princess Palace Program, you can check out (o) or quit (q).")
        if choice == "p" or choice == "P":
            byPrice()
        if choice == "pr" or choice == "PR" or choice == "Pr":
            byPrincess()
        if choice == "c" or choice == "C":
            byColor(input("What color room would you like to search for?").lower())
        if choice == "q" or choice == "Q" or choice == "o" or choice == "O":
            print("Thank you for using the Princess Palace Hotel Program. Come again soon!")
            break

#main
PrincessPalaceMenu()


