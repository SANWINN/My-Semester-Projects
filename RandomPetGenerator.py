#Saniya Winn
#Random Pet Generator
#2/21/2025

#Init
import random
import time
from PIL import Image
import requests
from io import BytesIO
PetList = ["https://tinyurl.com/mr22taek", #dog, InsideDogsWorld, no author, https://tinyurl.com/mr22taek, Doggy DNA – Learn How to Determine Your Dog’s Breed,  June 15, 2017,
"https://tinyurl.com/yrvpn4vw", #cat, Reader's Digest, Christophe Lehenaff, https://tinyurl.com/yrvpn4vw, 17 Long-Haired Cat Breeds That Have Seriously Impressive Locks, Jul. 29, 2023, License our Content © 2025 Trusted Media Brands, Inc.
"https://tinyurl.com/ydpuj2n5", #Koi Story, nA, https://tinyurl.com/ydpuj2n5, A Beginner's Guide to Raising Koi Fish, nD, Copyright ® 2013-2022 by Big Picture Web, LLC dba Koistory
"https://tinyurl.com/5fhbdwbz", #hamster, ZooPlus, nA, https://tinyurl.com/5fhbdwbz, Hamster Language, 11/06/2024, zooplus Magazine published by zooplus SE © zooplus SE 2025
"https://tinyurl.com/5fepxj9s" #snake, ReptileFact, nA, https://tinyurl.com/5fepxj9s, Ball Python Facts and Pictures, nD, nC
]

#Functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def PetGenerator():
print("Welcome to Pet Recommender! This program was created to help you choose a pet!")
while True:
    begin = input("Would you like a recommendation for a possible pet?")
    if begin == "Y" or begin == "y":
        url = random.choice(PetList)
        open_image(url)
        time.sleep(2)
        if url == "https://tinyurl.com/mr22taek":
            print("""Your recommendation is a dog! Dogs have a great sense of smell,
and amazing communication skills! They come in a wide range of breeds,
each with unique roles and physical features!""")
        if url == "https://tinyurl.com/yrvpn4vw":
            print("""Your recommendation is a cat! Cats have excellent distance vision,
and they're communication champs! Cats are incredibly agile and have impressive reflexes,
allowing them to land on their feet.""")
        if url == "https://tinyurl.com/ydpuj2n5":
            print("""Your recommendation is a koi fish! Joi fish are originally from Japan,
and are known for their vibrant colors and patterns! They can live between 25-50 years on average!""")
        if url == "https://tinyurl.com/5fhbdwbz":
            print("""Your recommendation is a hamster! These timid rodents are
among the popular small pets,and love exploring and using their whiskers to help
them sense objects in their environment!""")
        if url == "https://tinyurl.com/5fepxj9s":
            print("""Your recommmendation is a snake! These beautiful
limbless reptiles are found almost everywhere, and can hear despite
having no external ears! They come in all shapes and sizes, and are
the best scaly friends to have!""")
    if begin == "n" or begin == "N":
        print("Alright, come back soon.")
        break
#Main
PetGenerator()
