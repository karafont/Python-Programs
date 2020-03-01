CPM = 4.2

print ('Calories burned per minute:')

for time in range(10, 31, 5):
    calories_burned = CPM * time
    print (time, '\t', calories_burned)
