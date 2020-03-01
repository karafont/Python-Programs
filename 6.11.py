def getName():
  userName = input ( "Enter your name: " )
  return userName

def getBio():
  userBio = input ( "Please enter a sentence or two that describes yourself: " )
  return userBio

def webPage(userName, userBio):
  web = "biopage.html"
  openFile = open(web, "w+")
  
  openFile.write("<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>"+userName+"</h1>\n\t</center>\n\t<hr />\n\t"+userBio+"\n\t<hr />\n</body>\n</html>")

  openFile.close()

def main():
    userName = getName()
    userBio = getBio()
    webPage(userName, userBio)

main()