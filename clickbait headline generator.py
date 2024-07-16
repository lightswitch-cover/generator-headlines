#Nora Rogozinski
#7/15
#Clickbate Headline Generator
\
#Initialization
import random

#Functions
def unusualDIYS():
    object = input("Enter a plural object:")
    number = input("Enter a number 5-10:")
    number2 = input("Enter a number 1-5:")
    return (number + " Uses For " + object + " You Would Have Never Though Of (#" + number2 + " Will Suprise You!)")
    unusualDIYS = "1"
def celebNews():
    state = input("Enter state:")
    action = input("Enter an action:")
    celebrity = input("Enter Celebrity:")
    agreement = input("Enter: Man, Woman, or Person:")
    return (state + " " + agreement + " " + action + " Into " + celebrity + ", You'll Never Guess What Happened Next")

def lawsuit():
    food = input("Enter food:")
    store = input("Enter grocery store name:")
    return ("Recall On " + food + " From " + store + " Make Hundreds Ill, Are You Elidgeible To Join The Lawsuit?")

def politicalJoke():
    party = input("Enter political party:")
    money = input("Enter number:")
    leader = input("Enter politician:")
    return (party + " Represenatives Found With " + money + " Million In Stolen Cash, " + leader + "'s Response Will Shock You")

def millionaireNews():
    millionaire = input("Enter millionaire:")
    amount = input("Enter number:")
    prize = input("Enter number:")
    return (millionaire + " Giving Away " + amount + " Million In Checks, Sign Up Now For A Chance To Win " + prize + " Thousand Dollars!")

def headlineWriter():
    print("Welcome To Clickbait Headliner Generator! Pick A Prompt To Begin")
    print("1. Unusual DIY's \n 2. Celebrity News \n 3. Lawsuit \n 4. Political News \n 5. Millionaire News \n 6. Random")
    choice = input("Enter Number Selection:")
    if choice == "1":
        unusualDIYS()
    elif choice == "2":
        celebNews()
    elif choice == "3":
        lawsuit()
    elif choice == "4":
        politicalJoke()
    elif choice == "5":
        millionaireNews()
    elif choice == "6":
        x = random.randint(1,5)
        if x == 1:
             return(unusualDIYS())
        elif x == 2:
             return(celebNews())
        elif x == 3:
            return(lawsuit())
        elif x == 4:
            return(politicalJoke())
        elif x == 5:
            return(millionaireNews())

#Main
headlineWriter()