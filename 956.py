# swap_lists
# -----
# This function takes two lists of equal length 
# as arguments and swaps their values.
def swap_lists(first, second):
    if len(first) != len(second):
        print "Lengths must be equal!"
        return
    
    for i in range(len(first)):
        first_current_i = first[i]
        first[i] = second[i]
        second[i] = first_current_i

list_one = [1, 2, 3]
list_two = [4, 5, 6]

print "Before swap"
print "list_one: " + str(list_one)
print "list_two: " + str(list_two)

swap_lists(list_one, list_two)

print "After swap"
print "list_one: " + str(list_one)
print "list_two: " + str(list_two)
