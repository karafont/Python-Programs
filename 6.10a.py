def getName():
    golferName = input ( "Please enter the golfer's name: ")
    return golferName

def getScore(golferName):
    golferScore = input ( "Please enter "+ golferName +"'s score: ")
    return golferScore

def main():
    golfFile = open("golf.txt", "w")
   
    anotherPlayer = "y"

    while anotherPlayer == "y" or anotherPlayer == "Y":
        golferName = getName()
        golferScore = getScore(golferName)

        golfFile.write( golferName + "\n" + golferScore + "\n") 

        anotherPlayer = input ( "Do you have another golfer to enter? " + \
             "Type 'Y' for yes or any other character for no: ")

    golfFile.close()

    print ( "Your entry has been recorded in golf.txt. Thank you." )

main()
