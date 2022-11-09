# practicing functions
# by Pedro Echavarria
#***********************
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
from math import degrees, factorial, log
import random
import turtle
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
#__________________________________________________________________________________________________

# Write a program that gets a string as input from the user, and finds the index of the first
# occurrence of the letter ‘u’ (upper or lower case). Your program should define a function
# that takes a string as a parameter and returns the u index. If the string does not contain a
# u, the function should return -1. No library functions aside from input/output.

# Example call          Returns
# find_u(“OUCH”)           1
# find_u(“oops”)          -1

def find_u(str):
    fricative = 'u'
    count = 0
    for i in str:
        for consonants in fricative.upper():
            count += i.upper().count(consonants)
            # print(count)
    if count >= 1:
        return 1
    else:
        return -1
                
print(find_u("OUCH"))
print(find_u("oops"))
#__________________________________________________________________________________________________

def well(x):
    t = -3
    while t < x:
        if t < 0:
            t += x
        else:
            t *= 2
    return t 

#__________________________________________________________________________________________________

def why11(list):
    y = 1
    j = 0
    while j < len(list) and y < 11:
        x = list[j]
        if x < 0:
            y -= x
        elif x % 2 == 0:
            y *= x
        else:
            y += x
        j += 2
    return y
print(why11([4,-1,-5,2,1,3,7,-8]))
        
#__________________________________________________________________________________________________

# Function that takes a list of strings as a parameter and returns the number of fricative
# consonants (f, s, v, z) occurring in the list

# Example function call:

# Outputs: 3

def count_fricatives(list):
    fricative = 'fsvz'
    count = 0
    for i in list:
        for consonants in fricative.upper():
            count += i.upper().count(consonants)
    return count

list = ['Zebra', 'light saber', '1234 JOYS!']
print(count_fricatives(list))
print(count_fricatives(list) == 3)
#__________________________________________________________________________________________________

# while loop that repeatedly prompts the user to enter a number (“Q” to quit) and counts 
# the total number of zeroes entered by the user.

# Example program run:

# > Enter a number (‘Q’ to quit)? 750
# > Enter a number (‘Q’ to quit)? 405
# > Enter a number (‘Q’ to quit)? 100
# > Enter a number (‘Q’ to quit)? Q
# > You entered 4 zeroes

contar = ""
name = "Q"
while True:
    num = input("enter a number (“Q” to quit)? ")
    if num != name :
        contar += num # type: ignore
        result = contar.count("0") # type: ignore
    else:
        print("You entered", result + " Zeros") # type: ignore
        break

#__________________________________________________________________________________________________

# Program that asks the user for their favorite month and day of the month as input and outputs
# The month & day followed by the year, Whether or not the month is alphanumeric, The number of
# 2’s in the number The factorial of the number and The log base 2 of the absolute value of the number.

def day():
    favorite_month = input("Please enter your favorite month: ")
    favorite_day = input("Enter your favorite day of the month: ")
    str1 = favorite_month[0].upper()
    str2 = favorite_month[1:].lower()
    print(str1 + str2, favorite_day , ", 2020")
    print("Is the month alphanumeric?", favorite_month.isalnum())
    print("How many 2’s?",favorite_day.count("2"))
    favorite_day = int(favorite_day)
    print("Factorial: ", factorial(favorite_day)) 
    print("Log base 2: ", log(abs(favorite_day), 2)) 

day()
#__________________________________________________________________________________________________