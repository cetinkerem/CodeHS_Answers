# Write your function here...
def safe_int(target):
    try:
        return int(target)
    except ValueError:
        return 0

list_of_strings = ["a", "2", "7", "zebra"]


# Your code here...

print [safe_int(x) for x in list_of_strings]
