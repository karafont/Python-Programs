userPurchase = float(input("Please enter the amount of your purchase: "))

STATETAX = 0.05 * userPurchase

COUNTYTAX = 0.025 * userPurchase

totalTax = STATETAX + COUNTYTAX

totalSale = userPurchase + totalTax

print ("\nAmount of purchase $" + format(userPurchase, ",.2f" ), \
    "State Tax: $" + format( STATETAX, ",.2f" ), "County tax: $" + \
    format( COUNTYTAX, ",.2f" ), "Total Tax: $" + format ( totalTax, ",.2f" ), \
    "Total sale: $" + format( totalSale, ",.2f" ), sep = "\n" )
