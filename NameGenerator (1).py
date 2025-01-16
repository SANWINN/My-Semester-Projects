#Saniya Winn
#10/18/2024
#Period 5
#Name Generator Project

print("Welcome to Your Simpsons Character 2000!")
print("Answer questions to find out which Simpsons character you are!")
ans = input("Coffee (c) or Tea (t)?")
if ans == "c":
    ans = input("Gryffindor (g) or Slytherin (s)?")
    if ans == "g":
        ans = input("Lazy (l) or Energetic (e)?")
        if ans == "l":
            print("Your Simpsons character is ... Homer Simpson!")
        else:
            print("Your Simpsons character is ... Krusty the Clown!")
    else:
        input("Shout (s) or Whisper (w)?")
        if ans == "s":
            print("Your Simpsons character is ... Bart Simpson!")
        else:
            print("Your Simpsons character is ... Lisa Simpson!")
else:
    input("Ravenclaw (r) or Hufflepuff (h)?")
    if ans == "r":
        ans = input("Power (p) or Morals (m)?")
        if ans == "p":
            print("Your Simpsons character is ... Mr. Burns!")
        else:
            print("Your Simpsons character is ... Marge Simpson!")
    else:
        ans = input ("Relaxed (r) or Anxious (a)?")
        if ans == "r":
            print("Your Simpsons character is ... Ned Flanders!")
        else:
            print("Your Simpsons character is ... Milhouse Van Houten!")
