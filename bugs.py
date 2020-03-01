total = 0

for day in range(1, 8):
    print ('Enter the total number of bugs collected on day', day, ':')
    bugs = int (input ())
    total += bugs

print ('You collected a total of', total, 'bugs.')
