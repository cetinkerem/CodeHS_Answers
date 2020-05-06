import random

# These lists will be used as tests in your check_values function
computer_list = [1,2,3,5];
user_list = [2,7,3,4];


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
        
    return colors    


print check_values(user_list, computer_list)
