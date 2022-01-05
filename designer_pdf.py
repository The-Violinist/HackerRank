# Find area taken up by the characters in a given word

# Height of all letters in alphabet
h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
# Word being considered
word = "abc"

def designerPdfViewer(h, word):
    highest = 0
    for letter in word:
        # Index of letter
        index = ord(letter) - 97
        # Change index to 
        height = h[index]
        if height > highest:
            highest = height
    return highest * len(word)
    
print(designerPdfViewer(h,word))