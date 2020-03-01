totalNumberMonths = 0
totalInchesRainfall = 0
numberOfYears = int (input ("Please enter the number of years: "))


for currentYear in range (1, numberOfYears +1):
    for currentMonth in range (1, 13):
        monthlyInches = float (input ("Please enter the number of inches of"+ \
                                " rainfall for month "+ format(currentMonth, "d")+ ":"))
        totalNumberMonths += 1
        totalInchesRainfall += monthlyInches


averageRainfall = totalInchesRainfall / totalNumberMonths

print ("Number of Months: " + format(totalNumberMonths, "d")+ ". Total inches of rainfall: "+\
       format(totalInchesRainfall, ".2f")+ ". Average Rainfall: "+ format(averageRainfall, ".2f"))

