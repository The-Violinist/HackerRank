# Designer PDF
# https://www.hackerrank.com/challenges/designer-pdf-viewer
# Find area taken up by the characters in a given word based on word length and the height of the highest letter

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]               # Sample height of all letters in the alphabet
word = "abc"                                                            # Word being considered

def designerPdfViewer(h, word):
    highest = 0
    for letter in word:
        index = ord(letter) - 97                                        # Find the index of the letter in the array based on its ASCII value
        height = h[index]                                               # Find the height of that letter based on the index
        if height > highest:                                            # Determine the highest letter
            highest = height
    return highest * len(word)                                          # Calculate the area by multiplying the height of the highest letter by the lenght of the word
    
print(designerPdfViewer(h,word))