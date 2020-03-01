vegetarian = input("Is anyone in your party vegetarian? Enter 'yes' or 'no': ")
vegan = input("Is anyone in your party vegan? Enter 'yes' or 'no': ")
gluten_free = input("Is anyone in your party gluten-free? Enter 'yes' or 'no': ")

if vegetarian != 'yes' and vegetarian != 'no':
    print("Your response was invalid, please try again and enter 'yes' or 'no'.")
    vegetarian = input("Is anyone in your party vegetarian? Enter 'yes' or 'no': ")
if vegan != "yes" and vegan != "no":
    print("Your response was invalid, please try again and enter 'yes' or 'no'.")
    vegan = input("Is anyone in your party vegan? Enter 'yes' or 'no': ")
if gluten_free != "yes" and gluten_free != "no":
    print("Your response was invalid, please try again and enter 'yes' or 'no'.")
    gluten_free = input("Is anyone in your party gluten free? Enter 'yes' or 'no': ")

if vegetarian == "yes":
    vegetarian = True
if vegetarian == "no":
    vegetarian = False
if vegan == "yes":
    vegan = True
if vegan == "no":
    vegan = False
if gluten_free == "yes":
    gluten_free = True
if gluten_free == "no":
    gluten_free = False

if vegetarian == True:
    if vegan == True:
        if gluten_free == True:
            print ("Here are your restaurant options: The Chef's Kitchen, Corner Cafe")
        elif gluten_free == False:
            print ("Here are your restaurant choices: Corner Cafe, The Chef's Kitchen")
    elif vegan == False:
        if gluten_free == True:
            print ("Here are your restaurant choices: Main Street Pizza Company, Corner Cafe, The Chef's Kitchen")
        elif gluten_free == False:
            print ("Here are your restaurant choices: Main Street Pizza Company, Corner Cafe, Mama's Fine Italian, "\
                    "The Chef's Kitchen")
elif vegetarian == False:
    if vegan == True:
        if gluten_free == True:
            print ("Here are your restaurant choices: Corner Cafe, The Chef's Kitchen")
        elif gluten_free == False:
            print ("Here are your restaurant choices: Corner Cafe, The Chef's Kitchen")
    elif vegan == False:
        if gluten_free == False:
            print ("Here are your restaurant choices: Joe's Gourmet Burgers, Main Street Pizza Company, "\
                    "Corner Cafe, Mama's Fine Italian, The Chef's Kitchen")
        elif gluten_free == True:
            print ("Here are your restaurant choices: Main Street Pizza Company, Corner Cafe, The Chef's Kitchen")

