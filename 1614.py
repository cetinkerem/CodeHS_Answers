def get_guess():
    acceptable_input = False
    
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


def out_of_range(numbers_list):
    for number in numbers_list:
        if not (1 <= number and number <= 7):
            return True
    return False

print get_guess()
