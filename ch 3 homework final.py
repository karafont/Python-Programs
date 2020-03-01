la_quinta = "La Quinta"
quality_inn = "Quality Inn"
holiday_inn = "Holiday Inn"
wingate = "Wingate"
country_inn = "Country Inn"
town_place = "TownPlace"
courtyard = "Courtyard"

pool = input('Do you need a pool at your hotel? Please answer "yes" or "no": ')
microwave = input('Do you need a microwave at your hotel? Please answer "yes" or "no": ')
restaurant = input('Do you need a restaurant at your hotel? Please answer "yes" or "no": ')


if pool == "yes":
    if microwave == "yes":
        if restaurant == "yes":
            print ("Here is your hotel choice:", holiday_inn)
        elif restaurant == "no":
            print ("Here is your hotel choice:", holiday_inn)
    elif microwave == "no":
        if restaurant == "yes":
            print ("Here are your hotel choices:", holiday_inn+ ",", wingate)
        elif restaurant == "no":
            print ("Here are your hotel choices:", holiday_inn+ ",", wingate+ ",", country_inn)
elif pool == "no":
    if microwave == "yes":
        if restaurant == "yes":
            print ("Here is your hotel choice:", holiday_inn)
        elif restaurant == "no":
             print ("Here are your hotel choices:", la_quinta+ ",", holiday_inn+ ",", quality_inn)
    elif microwave == "no":
            if restaurant == "yes":
                print ("Here are your hotel choices:", holiday_inn+ ",", wingate+ ",", town_place)
            elif restaurant == "no":
                print ("Here are your hotel choices:", la_quinta+ ",", quality_inn+ \
                       ",", holiday_inn+ ",", wingate+ ",", country_inn+ ",", town_place+ ",", courtyard)
elif pool != "yes" or pool != "no":
    print ('Your response was not recognized. Please try again and answer "yes" or "no" to each prompt.')
elif microwave != "yes" or microwave != "no":
    print ('Your response was not recognized. Please try again and answer "yes" or "no" to each prompt.')
elif restaurant != "yes" or pool != "no":
    print ('Your response was not recognized. Please try again and answer "yes" or "no" to each prompt.')
