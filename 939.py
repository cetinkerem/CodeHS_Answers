
first = input("First name: ")
last = input("Last name: ")

print("Full name: %s %s" % (first, last))

first, last = last, first

print("Citation: %s, %s" % (first, last))
