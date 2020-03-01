REGULARBATCH=48
REGULARSUGAR=1.5
REGULARBUTTER=1
REGULARFLOUR=2.75

userNumberOfCookies=float(input("How many cookies do you want to make? "))

expectedSugar= (userNumberOfCookies / REGULARBATCH)*REGULARSUGAR
expectedButter= (userNumberOfCookies / REGULARBATCH)*REGULARBUTTER
expectedFlour= (userNumberOfCookies / REGULARBATCH)*REGULARFLOUR

print("For " + str( userNumberOfCookies ) + " cookies, you will need " + \
      format( expectedSugar, ".2f" ) + " cup(s) of sugar, " + \
      format( expectedButter, ".2f" ) + " cup(s) of butter and " + \
      format( expectedFlour, ".2f") + " cup(s) of flour " )
