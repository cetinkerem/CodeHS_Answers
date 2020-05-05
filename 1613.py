import random

def create_comp_list():
    end_list = []
    
    for i in range(4):
        
        next_int = random.randint(1, 7)
        while next_int in end_list:
            next_int = random.randint(1, 7)
    
        end_list.append(next_int)
        
    return end_list

print create_comp_list()
