user_budget = float (input ('Please enter how much you have budgeted for the month: '))

more_expenses = 'y'
total_expenses = 0

while more_expenses == 'y':
    expense = float (input ('Please enter an expense: '))
    total_expenses += expense

    more_expenses = input ('Would you like to enter another expense? Enter "y" for yes,' \
                           ' any key for no: ')


end_budget = user_budget - total_expenses

if user_budget > total_expenses:
    print ('You are under your budget of $'+ format(user_budget, ',.2f'), 'by $'+ \
           format(user_budget - total_expenses, ',.2f'))

elif end_budget < 0:
        print ('You are over your budget of $'+ format(user_budget, ',.2f'), 'by $'+ \
           format(total_expenses - user_budget, ',.2f'))
else:
    print ('You used exactly your budget of $'+ format(user_budget, ',.2f'))
