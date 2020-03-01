def main():
    try:
        numFile = open( "numbers.txt", "r")

        total = 0
        numLines = 0 
        line = numFile.readline()
    

        while line != "":
            numLines += 1
            total += int( line )

            line = numFile.readline()

        average = total / numLines


    except IOError as error:
        print ( "An IOError has occurred:", error)
    
    except ValueError as error:
        print ( "A ValueError has occurred:", error)
    
    else: 
        print ( "The average of the numbers is", average )

    finally:
        numFile.close()
        print ("End of program.")

main ()
