MAX_TEMP = 102.5

vat_temp = float (input ('Please input the current vat temperature: '))

while vat_temp >= MAX_TEMP:
    print ('Please turn down the vat thermostat, wait five minutes,' \
           'then check the temperature again.')
    vat_temp = float (input ('Please reenter the vat temperature, given that' \
                             'you have turned down the thermostat for five minutes: '))

print ('The temperature of the vat is acceptable. Please wait 15 minutes and' \
       'check again. Thank you')
            
        
