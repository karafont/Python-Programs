import random

userPot = float (input ("How much money would you like to play with? "))

readyToPlay = True
totalGuesses = 0
highestTurn = 0
highestPot = 0
    
while readyToPlay == True:
    userNumber = int (input ("Please enter a number between 2-12: "))

    if userNumber < 2 or userNumber > 12:
        print ("You have entered an invalid number.")
        userNumber = int( input ("Please enter a number between 2-12: "))

    computerGuess = random.randint (2, 12)
    totalGuesses += 1

    if userNumber != computerGuess:
        userPot -= 1
        print ( "The computer rolled \t", computerGuess, " You have $"+ format(userPot, ".2f"),\
               "available.")
        
    if userNumber == computerGuess:
        userPot += 3
        
        if userPot >= highestPot:
            highestPot = userPot
            highestTurn = totalGuesses
        print ( "The computer rolled \t", computerGuess, " You have $"+ format(userPot, ".2f"),\
               "available. \t YOU WIN!!!")

    if userPot == 0:
           readyToPlay = False

if userPot == 0 and highestPot > 0:
    print ("You are broke after", totalGuesses, "rolls.")
    print ("You should have quit after", highestTurn, "rolls when you had $"+ format(highestPot, ".2f"), ".")

if userPot == 0 and highestPot == 0:
    print ("You are broke after", totalGuesses, "rolls.")
    print ("You did not guess any rolls correctly, bad luck!")
