def main ():
    print("Info Report")
    state = getState()
    city = getCity()
    zip = getZip()
    print(city + ",", state + ",", zip)

def getState():
    state = input("What is the state? ")
    return state

def getCity():
    city = input("What is the city? ")
    return city

def getZip ():
    zip = input("What is the zip? ")
    return zip

main()
