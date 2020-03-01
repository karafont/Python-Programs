def main():
    golfFile = open("golf.txt", "r")

    golferName = golfFile.readline().rstrip( "\n" )

    while golferName != "":
        golferScore = golfFile.readline().rstrip( "\n" )

        print (golferName, "scored", golferScore, "points.")

        golferName = golfFile.readline().rstrip( "\n" )
    
    golfFile.close()

main()
