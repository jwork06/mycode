#!/usr/bin/env python3

print("Take this quiz to find out which Hogwarts house you are in!")
message = 'The sorting hat says: '
counter = 0

while counter < 3:
    Q1 = input("Which do you covet most: Love, Power, Wisdom, or Glory? ")
    if Q1.lower() == "love":
        message = message + 'Hufflepuff'
        print(message)
        break
    elif Q1.lower() == "power":
        message = message + 'Slytherin'
        print(message)
        break
    elif Q1.lower() == "wisdom":
        message = message + 'Ravenclaw'
        print(message)
        break
    elif Q1.lower() == "glory":
        message = message + 'Gryffindor'
        print(message)
        break
    else:
        message = "Invalid input. Please try again."
        counter += 1    
   
    print(message)
