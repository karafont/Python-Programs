def main():
    numFile = open( "numbers.txt", "r")

    total = 0
    numLines = 0 
    line = numFile.readline()
    

    while line != "":
        numLines += 1
        total += int( line )

        line = numFile.readline()

    average = total / numLines

    print ( "The average of the numbers is", average )

    numFile.close()
    print ("End of program.")

main ()
