"""
Guess The Word, Part 2
"""


secret_word = "helicopter"
dashes = "----------"


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


def update_dashes(guess):
    return_dashes = ""
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            return_dashes += guess
        else:
            return_dashes += dashes[i]
    return return_dashes

while 1:
    print dashes
    next_guess = get_guess()
    dashes = update_dashes(next_guess)
    
