"""
Guess The Word, Part 3
"""


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


secret_word = "helicopter"
dashes = "----------"

guesses_left = 10

print str(guesses_left) + " incorrect guesses left.\n"

while dashes != secret_word and guesses_left != 0:
    print dashes
    
    next_guess = get_guess()
    
    if next_guess in secret_word:
        print "That is in the word!"
    else:
        print "That's not in the word"
        guesses_left -= 1
        print str(guesses_left) + " incorrect guesses left."
        
    
    dashes = update_dashes(next_guess)

if guesses_left != 0:
    print "Congrats, you got it! The word was " + secret_word
else:
    print "You lost. The secret word was " + secret_word
