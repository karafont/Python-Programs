def getName():
    name = input("What is your name? ")

    return name

def getAge():
    age = int(input("What is your age? "))

    return age

def printCompany():
    print("Sam's Swimwear \nEmployee Report", sep="\n")

def printNameAge(name, age):
    print( "Your name is", name+ ". Your age is", str(age)+ "." )

def main():
    name = getName()
    age = getAge()
    printCompany()
    printNameAge( name, age)

main()
