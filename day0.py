# Day 1 : Division and Square-root
# Challenge : Write a function called divide_or_square that takes one argument (a number)
#             and returns the square root of the number if it is divisible by 5, returns it
#             remainder if it is not divisible by 5.
import math
def divide_or_square(int):
    if(int % 5 == 0):
        return math.sqrt(int)
    if(int % 5 != 0):
        return int % 5

print(divide_or_square(14))
print(divide_or_square(10))

# Extra challenge: Longest Value
#   Write a function called longest_value that takes a dictionary as as 
#   argument and returns the first longest value of the dictionary. 

fruits = {
    'fruit':'apple',
    'color':'green'
} 

def longest_value(d):
    values = list(d.values())
    length = 0
    longest = ""
    for item in values:
        if len(item) > length:
            longest = item
            length = len(item)
    return longest


print(longest_value(fruits))

