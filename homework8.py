textToEdit = [ch for ch in open("sentences.txt").read() if ch != '\n']

leadChar = True
for ix, ch in enumerate(textToEdit):
    if leadChar and ch.isalpha():
        ch = ch.upper()
        
        textToEdit[ix] = ch
        
        leadChar = False
    if ch in '?!.':
        leadChar = True

capitalizedText = ''.join(textToEdit)

newText = open("newText.txt", "w")
newText.writelines(capitalizedText)
newText.close()
