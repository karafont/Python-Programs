
def userPurchase():
    userPurchase = float(input("Please enter the amount of your purchase: "))

    return userPurchase

def CalcStateTax( userPurchase ):
    stateTax = 0.05 * userPurchase

    return stateTax

def CalcCountyTax( userPurchase ):
    countyTax = 0.025 * userPurchase

    return countyTax

def CalcTotalTax( stateTax, countyTax):
    totalTax = stateTax + countyTax

    return totalTax

def CalcTotalSale( userPurchase, totalTax ):
    totalSale = userPurchase + totalTax

    return totalSale

def printDetails( userAmountPurchased, stateTax, countyTax, totalTax, totalSale):
    print ( "\nAmount of purchase $" + \
        format( userAmountPurchased, ",.2f" ), "State Tax: $" + \
        format( stateTax, ",.2f" ), "County tax: $" + \
        format( countyTax, ",.2f" ), "Total Tax: $" + \
        format( totalTax, ",.2f" ), "Total sale: $" + \
        format( totalSale, ",.2f" ), sep = "\n" )

def main():
    userAmountPurchased = userPurchase()
    stateTax = CalcStateTax( userAmountPurchased )
    countyTax = CalcCountyTax( userAmountPurchased )
    totalTax = CalcTotalTax( stateTax, countyTax )
    totalSale = CalcTotalSale( userAmountPurchased, totalTax )
    printDetails(userAmountPurchased, stateTax, countyTax, totalTax, totalSale)


main()
