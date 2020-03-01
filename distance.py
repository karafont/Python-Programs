vehicleSpeed = float (input ("Enter the MPH the vehicle is traveling: "))
timeTraveled = int (input ("Enter the length of time the vehicle has been traveling: "))

print ()

print ("Hour","\tDistance Traveled")
for currentHour in range (1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print (currentHour,"\t",distanceTraveled)
    
