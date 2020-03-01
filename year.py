import calendar
def main():
    aYear = get_4_digit_year()
    internalLeap = getLeapYear(aYear)
    aMonth = get_month()
    aDay = get_day(aYear,aMonth, internalLeap)
    print(aDay)

def get_4_digit_year():
    someYear = input("Please enter the 4-digit year: ")
    while not someYear.isnumeric() or len(someYear) != 4:
        print("ERROR - year must be a 4-digit number")
        someYear = input("Please enter the year again: ")
    return someYear

def getLeapYear(year):
    if (int(year)) % 400 == 0:
        return True
    if (int(year)) % 100 == 0:
        return False
    if (int(year)) % 4 == 0:
        return True
    else:
        return False

def get_day(aYear,aMonth, internalLeap):
    if int(aMonth) == 4 or \
       int(aMonth) == 6 or \
       int(aMonth) == 9 or \
       int(aMonth) == 11:
           aDay = checkDay(aYear,30)
    elif int(aMonth) == 2:
        fakeYear = int(aYear)
        if calendar.isleap(fakeYear):
            functionLeap = True
            aDay = checkDay(aYear,29)
        else:
            functionLeap = False
            aDay = checkDay(aYear,28)
    else:
        aDay = checkDay(aYear,31)
    print ("functionLeap=", functionLeap)
    print("internalLeap=", internalLeap)
    return aDay
           
def checkDay(aYear,high):
    someDay = input("Please enter the day 1-"+ str(high)+": ")
    while not someDay.isnumeric() or \
          int(someDay) < 1 or \
          int(someDay) > high:
        print("ERROR - day must be 1-", high)
        someDay = input("Please enter the Day again: ")
    return someDay    


def get_month():
    someMonth = input("Please enter the month 1-12: ")
    while not someMonth.isnumeric() or \
          int(someMonth) < 1 or \
          int(someMonth) > 12:
        print("ERROR - month must be 1-12")
        someMonth = input("Please enter the month again: ")
    return someMonth
main()
