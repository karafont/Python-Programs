def main ():
    number = 1
    total = getNumber( number )
    printNum( total )

def getNumber( number ):
    number = float(input("Enter a positive number, or a negative number to quit: "))
    total = 0
    while number > 0:
        total = total + number
        number = float(input("Enter a positive number, or a negative number to quit: "))
    
    return total
    
def printNum( total ):
    print("The total of the numbers you entered is:", format(total, ",.2f"))

main()
