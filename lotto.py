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

def ticketSoldOut():
    #No ticket left

    print(
"""
!!!   THERE IS NO TICKET LEFT!  !!!
"""
        )

def  insufficientTicket():
    #Insufficient Ticket

    print(
"""
!!!   INSUFFICIENT TICKET!  !!!
"""
        )

def restartSelection():
    #restart ticket amount selection

    print(
"""
!!!   TICKET SELECTION RESTART!  !!!
"""
        )

def dateCheck():
    #current date
    date = datetime.now().strftime('%Y-%m-%d')

    dateData = date.split("-")
    #dateData[0] will be year
    #dateData[1] will be month
    #dateData[2] will be day

    yearData = int(dateData[0])
    monthData = int(dateData[1])
    dayData = int(dateData[2])

    #today date
    print("Today date is (Year-Month-Day) :")
    print(date)

    print("Next lottery date is (Year-Month-Day) :")

    #condition check
    if dayData > 15 and dayData <= 31:
        day = 1
        month = monthData + 1
        year = yearData

        if month > 12:
            month = 1
            year = yearData + 1
        else:
            pass

    elif dayData == 1:
        day = 1
        month = monthData
        year = yearData

    elif dayData > 1 and dayData <= 15:
        day = 15
        month = monthData
        year = yearData
    
    print(str(year) + "-" + str(month) + "-" + str(day))


def ticketInput():
    #lottery draw MAX = 50
    lotteryTicket = 50
    allowedAmount = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    firstTicket = 0
    secondTicket = 0
    thirdTicket = 0
    ticketAmount = [firstTicket, secondTicket, thirdTicket]

    print(
"""
# A MAXIMUM OF 50 TICKETS CAN BE PURCHASED #
"""
        )

    #1st TIER
    while True:
        firstTicket = int(input("Input ticket(s) for TIER 1 drawing : "))

        if firstTicket in allowedAmount:
            break

        else:
            inputErrorMessage()

    lotteryTicket = lotteryTicket - firstTicket

    print("Ticket left : " + str(lotteryTicket))

    if lotteryTicket == 0:
        lotteryTicket = 0

        ticketAmount[0] = 0

        ticketSoldOut()

        ticketAmount[0] = firstTicket
        ticketAmount[1] = 0
        ticketAmount[2] = 0

        return ticketAmount
        
        chooseNumber()


    elif lotteryTicket < 0:

        insufficientTicket()
        restartSelection()
        ticketInput()

    else:
        pass

    #2nd TIER
    while True:
        secondTicket = int(input("Input ticket(s) for TIER 2 drawing : "))

        if secondTicket in allowedAmount:
            break

        else:
            inputErrorMessage()

    lotteryTicket = lotteryTicket - secondTicket

    print("Ticket left : " + str(lotteryTicket))

    if lotteryTicket == 0:
        lotteryTicket = 0

        ticketAmount[1] = 0

        ticketSoldOut()

        ticketAmount[0] = firstTicket
        ticketAmount[1] = secondTicket
        ticketAmount[2] = 0

        return ticketAmount
        
        chooseNumber()


    elif lotteryTicket < 0:

        insufficientTicket()
        restartSelection()
        ticketInput()

    else:
        pass

    #3rd TIER
    while True:
        thirdTicket = int(input("Input ticket(s) for TIER 3 drawing : "))

        if thirdTicket in allowedAmount:
            break

        else:
            inputErrorMessage()

    lotteryTicket = lotteryTicket - thirdTicket

    print("Ticket left : " + str(lotteryTicket))

    if lotteryTicket == 0:
        lotteryTicket = 0

        ticketAmount[2] = 0

        ticketSoldOut()

        ticketAmount[0] = firstTicket
        ticketAmount[1] = secondTicket
        ticketAmount[2] = thirdTicket

        return ticketAmount
        
        chooseNumber()


    elif lotteryTicket < 0:

        insufficientTicket()
        restartSelection()
        ticketInput()

    else:

        ticketAmount[0] = firstTicket
        ticketAmount[1] = secondTicket
        ticketAmount[2] = thirdTicket

        return ticketAmount

        chooseNumber()


    #return a ticket amount to another function
    
def chooseNumber(ticketAmount):
    #choose a number for each tier

    #


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
            rules()
            dateCheck()
            ticketInput()

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


introduction()

def ticketTransfer():
    #transfer a variable

    ticketAmount = ticketInput()

    chooseNumber(ticketAmount)

ticketTransfer()

menu()




