numbers = {}

while 1:
    answer = input("Please enter the desired name: ")
    
    if answer == "":
        break
    
    if answer in numbers:
        print answer + "'s phone number is " + str(numbers[answer])
    else:
        numbers[answer] = int(input("Unknown person. What is their number? "))
