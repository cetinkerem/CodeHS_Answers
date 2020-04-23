words = {}

words_in = input("Please enter input:\n\n")

for word in words_in.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        
print words
