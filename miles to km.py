def askUserForKM():
    userKilometers = float(input("Please enter the distance in kilometers: "))

    return userKilometers

def convertKMtoMiles( userKilometers ):
    miles = userKilometers * 0.6214

    return miles

def main ():
    userKilometers = askUserForKM()
    convertedMiles = convertKMtoMiles( userKilometers )

    print (userKilometers, "kilometers converted to miles is", \
           format(convertedMiles, ',.2f'), "miles.")

main()
