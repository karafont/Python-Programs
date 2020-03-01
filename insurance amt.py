def GetRebuildCost():
    rebuildCost = float(input("Please enter the amount of money that you"+ \
         " would need to rebuild your building: "))
    
    return rebuildCost

def GetInsuranceNeeded ( rebuildCost ):
    insuranceNeeded =  0.8 * rebuildCost

    return insuranceNeeded

def main():
    rebuildCost = GetRebuildCost()
    insuranceRec= GetInsuranceNeeded( rebuildCost )

    print ("Based on the rebuild value of your building, $"+ \
        format(rebuildCost, ",.2f")+ ", you should insure it for at least $"+ \
        format(insuranceRec, ",.2f"))

main ()
