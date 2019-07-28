import random
import time
import os
import time

from datetime import datetime

#initial a variable

sixDigit = random.randint(0, 999999)
rewardSixDigit = 5000000

threeDigit = random.randint(0, 999)
rewardThreeDigit = 30000

twoDigit = random.randint(0, 99)
rewardTwoDigit = 2000

lottoBuy = 50

def introduction():
    #intro to the program

    file = open('resource/Introduction.txt', 'r')
    print(file.read())
    file.close()

def credits():
    #credits file

    file = open('resource/Credits.txt', 'r')
    print(file.read())
    file.close()

def rules():
    #rules file

    file = open('resource/Game rules.txt', 'r')
    print(file.read())
    file.close()

def exit():
    #edit program

    print("Press ENTER key to quit..." '\n')

    userExit = input()

    quit()

def inputErrorMessage():
    #input error

    print(
"""
!!!   ERROR! INVALID INPUT.  !!!
"""
        )

def menu():
    #main menu

    print(
"""
Menu :
(1) Start game
(2) Game rules
(3) Credits
(9) Exit
"""
    )

    while True:
        print("For help, type : \"help\"")
        menuSelection = input("Menu selection : ")

        if menuSelection == "1":
            game()

        elif menuSelection == "2":
            rules()

        elif menuSelection == "3":
            credits()

        elif menuSelection == "9":
            exit()

        elif menuSelection == "help":
            menu()

        else:
            inputErrorMessage()

def game():
    #game core

    rules()

    #current date
    date = datetime.now().strftime('%Y-%m-%d')

    dateData = date.split("-")
    #dateData[0] will be year
    #dateData[1] will be month
    #dateData[2] will be day

    yearData = int(datetime[0])
    monthData = int(datetime[1])
    dayData = int(datetime[2])

    #today date and time
    print("Today time is (Year-Month-Day) :")
    print(date)

    print("Next lottery date is (Year-Month-Day) :")

    #condition check
    if dateData > 15:
        month = monthData + 1
        if month > 12:
            month = 1
            year = yearData + 1
        else:
            pass

    elif dateData >= 1 and dateData <= 15
        
















introduction()
menu()



