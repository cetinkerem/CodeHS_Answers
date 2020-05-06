import random

computer_list = [1,2,3,5];
user_list = [1,2,3,5];


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
    else:
        print colors


def check_win(response_list):
    return (response_list == ["RED", "RED", "RED", "RED"])


check_values(computer_list, user_list)
