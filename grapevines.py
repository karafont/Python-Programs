rowLength=float(input("How many feet long is the row? "))
endPostAssembly=float(input("How many feet will be used by the end-post? "))
spaceBetweenVines=float(input("How many feet are between the vines? "))


grapevinesInARow=(rowLength - (endPostAssembly*2)) / spaceBetweenVines

print("You should plant "+ format(grapevinesInARow, ".0f")+ " grapevines per row.")
