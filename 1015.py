"""
Guess The Word, Part 4
"""

import random


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


words = [
"absurd",
"abyss",
"affix",
"askew",
"avenue",
"awkward",
"axiom",
"azure",
"bagpipes",
"bandwagon",
"banjo",
"bayou",
"beekeeper",
"bikini",
"blitz",
"blizzard",
"boggle",
"bookworm",
"boxcar",
"boxful",
"buckaroo",
"buffalo",
"buffoon",
"buxom",
"buzzard",
"buzzing",
"buzzwords",
"caliph",
"cobweb",
"cockiness",
"croquet",
"crypt",
"curacao",
"cycle",
"daiquiri",
"dirndl",
"disavow",
"dizzying",
"duplex",
"dwarves",
"embezzle",
"equip",
"espionage",
"euouae",
"exodus"]

secret_word = random.choice(words)
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
    print "Congrats, You win! The word was " + secret_word
else:
    print "You lose! The secret word was " + secret_word
