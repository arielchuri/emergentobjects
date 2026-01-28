import random

# Using functions

# In this application we

goodOrEvil = "none"
evilFirstName = ["Dark", "Over", "Beast", "Shadow", "Witch", "Evil"]
goodFirstName = ["Super", "Star", "Robo", "Silver", "Time"]
lastName = ["Lord", "Surfer", "Master", "Entity", "Duck"]
def checkGoodOrEvil():
    global goodOrEvil
    while goodOrEvil != "a" and goodOrEvil != "b":
        print("Do you choose the path of (a) forgiveness or (b) vengeance?")
        goodOrEvil = input("Please enter the letter for your choice: ")
    if goodOrEvil == "a":
        print("You have chosen the path of forgiveness.")
    elif goodOrEvil == "b":
        print("You have chosen the path of vengeance")

def getSuperName(x):
    if x == "a":
        print("****** " + random.choice(goodFirstName) + " " + random.choice(lastName) + " ******")
    else:
        print("****** " + random.choice(evilFirstName) + " " + random.choice(lastName) + " ******")

print("*********************************")

checkGoodOrEvil()
print("You super name is:")
getSuperName(goodOrEvil)

print("Goodbye")
