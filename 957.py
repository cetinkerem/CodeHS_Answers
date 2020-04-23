words = {}


def update_counts(words, word):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


words_in = input("Please enter input:\n\n")

for word in words_in.split():
    update_counts(words, word)
        
print words
