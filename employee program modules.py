import agemod
import namemod

def main():
    name = ( namemod.getName() )
    age = ( agemod.getAge() )
    printCompany()
    printNameAge( name, age )

def printCompany():
    print( "Sam's Swimwear \nEmployee Report", sep="\n" )

def printNameAge( name, age ):
    print( "Your name is "+ name + ".\nYour age is " + str(age)+ ".", sep="\n" )

main()
