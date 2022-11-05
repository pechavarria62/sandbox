# NAME:         Pedro Echavarria
# ASSIGNMENT:   Project 1

# Example
from itertools import zip_longest


def hello_world():
    return "Hello!"

# 1
def squared_sum(array):
    sum = 0
    for i in array:
        sum += i ** 2
    return sum

# 2
def mix(a, b):
    x = a,b
    new_string = ''.join(''.join(x) for x in zip_longest(a, b,fillvalue=''))
    print(new_string)
    return new_string

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")
    
main()
