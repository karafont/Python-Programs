def getLoanAmt():
    loanAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car loan: "))

    return loanAmt

def getInsAmt():
    insAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car insurance: "))

    return insAmt

def getGasAmt():
    gasAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car's gas: "))

    return gasAmt

def getOilAmt():
    oilAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car's oil: "))

    return oilAmt

def getTiresAmt():
    tiresAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car's tires: "))

    return tiresAmt

def getMaintAmt():
    maintAmt = float(input("Please enter the monthly amount you spend on your"+\
        " car's general maintenance: "))

    return maintAmt

def CalcMonthlySum( gasAmt, oilAmt,  tiresAmt,  maintAmt,  loanAmt,  insAmt ):
    monthlySum = gasAmt + oilAmt + tiresAmt + maintAmt + loanAmt + insAmt

    return monthlySum

def CalcAnnualSum ( monthlySum ):
    annualSum = monthlySum * 12

    return annualSum

def main():
    loanAmt = getLoanAmt()
    insAmt = getInsAmt()
    gasAmt = getGasAmt()
    oilAmt = getOilAmt()
    tiresAmt = getTiresAmt()
    maintAmt = getMaintAmt()
    monthlySum = CalcMonthlySum (gasAmt, oilAmt,  tiresAmt,  maintAmt,  loanAmt,  insAmt)
    annualSum = CalcAnnualSum ( monthlySum )

    print ("Based on your input, you spend $"+ format(monthlySum, ",.2f"), 
        "per month on your car's upkeep. Annually, you spend $"+ \
        format(annualSum, ",.2f"), "on your car's upkeep.")

main()
    
