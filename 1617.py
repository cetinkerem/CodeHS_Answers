import random

def get_guess():
    acceptable_input = False
    raw_guess_numbers = []
    
    while not acceptable_input:
        try:
            raw_guess_numbers = [int(x) for x in input("Enter your guess: ")]
        
            if len(raw_guess_numbers) != 4:
                print "Your guess must be 4 numbers long!"
                continue
            
            if out_of_range(raw_guess_numbers):
                print "All numbers must be between 1 and 7!"
                continue
                
            if len(raw_guess_numbers) != len(set(raw_guess_numbers)):
                print "No duplicate numbers allowed!"
                continue
            
            acceptable_input = True
        except ValueError:
            print "You must only use numbers!"
            
    return raw_guess_numbers


def out_of_range(numbers_list):
    for number in numbers_list:
        if not (1 <= number and number <= 7):
            return True
    return False


def check_values(user, computer):
    colors = []
    
    shuffled = user[:]
    random.shuffle(shuffled)
    for number in shuffled:
        if number in computer:
            input_number_pos = user.index(number)
            computer_number_pos = computer.index(number)
            if input_number_pos == computer_number_pos:
                colors.append("RED")
            else:
                colors.append("WHITE")
        else:
            colors.append("BLACK")
        
    if check_win(colors):
        print "Congratulations! You got it"
        return True
    else:
        print colors
        return False


def check_win(response_list):
    return (response_list == ["RED", "RED", "RED", "RED"])


def create_comp_list():
    end_list = []
    
    for i in range(4):
        
        next_int = random.randint(1, 7)
        while next_int in end_list:
            next_int = random.randint(1, 7)
    
        end_list.append(next_int)
        
    return end_list


def play_game():
    numbers = create_comp_list()
    guesses = 5
    while guesses > 0:
        print "Guesses left: " + str(guesses)
        
        if check_values(get_guess(), numbers):
            return
        
        guesses = guesses - 1
    
    print "You lost. The numbers were " + str(numbers)
    

# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.
print "Play the game now, yay....."


play_game()
