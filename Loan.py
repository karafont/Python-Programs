MIN_SALARY = 30000
MIN_YEARS = 2

salary = float(input("Enter your annual salary: "))
years_on_job = float(input("Enter the number of years employed: "))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print("You qualify for the loan, congratulations!")
    else:
        print("You must have been employed for at least", MIN_YEARS, \
              "to qualify for the loan.")

else:
    print('You must earn at least $'+ format(MIN_SALARY, ',.2f'), ' per year to qualify.', sep='')
        
                    
