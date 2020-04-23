"""
Guess The Word, Part 1
"""


secret_word = "helicopter"


def get_guess():
    while 1:
        guess = input("Guess a letter: ")
        
        if len(guess) != 1:
            print "Must be exactly one letter."
            continue
        
        if not guess.isalpha():
            print "Must be alphabetical."
            continue
        
        return guess.lower()


while 1:
    print get_guess() in secret_word
