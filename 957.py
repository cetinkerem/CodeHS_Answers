count_dictionary = {}


def update_counts(count_dictionary, word):
    if word in count_dictionary:
        count_dictionary[word] += 1
    else:
        count_dictionary[word] = 1


words_in = input("Please enter input:\n\n")

for word in words_in.split():
    update_counts(count_dictionary, word)
        
print count_dictionary
