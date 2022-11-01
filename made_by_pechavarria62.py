# (((((((((((((((((((((( by Pedro Echavarria ))))))))))))))))))))))

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))
from re import X
import turtle
import random

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

#__________________________________________________________________________________________________

# while loop that repeatedly prompts the user to enter a number (“Q” to quit) and counts 
# the total number of zeroes entered by the user.

# Example program run:

# > Enter a number (‘Q’ to quit)? 750
# > Enter a number (‘Q’ to quit)? 405
# > Enter a number (‘Q’ to quit)? 100
# > Enter a number (‘Q’ to quit)? Q
# > You entered 4 zeroes

# contar = ""
# name = "Q"
# while True:
#     num = input("enter a number (“Q” to quit)? ")
#     if num != name :
#         contar += num # type: ignore
#         total = contar.count("0") # type: ignore
#     else:
#         print("You entered", total, "Zeros")# type: ignore
#         break

#__________________________________________________________________________________________________

# Function that takes a list of strings as a parameter and returns the number of fricative
# consonants (f, s, v, z) occurring in the list

# Example function call:

# Outputs: 3

# def count_fricatives(list):
#     fricative = 'fsvz'
#     count = 0
#     for i in list:
#         for consonants in fricative.upper():
#             count += i.upper().count(consonants)
#     return count

# list = ['Zebra', 'lightsaber', '1234 JOYS!']
# print(count_fricatives(list))
# print(count_fricatives(list) == 3)

#__________________________________________________________________________________________________

'''def well(x):
    t = -3
    while t < x:
        if t < 0:
            t += x
        else:
            t *= 2
    return t '''

#__________________________________________________________________________________________________

'''def why11(list):
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
print(why11([4,-1,-5,2,1,3,7,-8]))'''
        

#__________________________________________________________________________________________________

# answers:
# 17

#  a S mer! py Su 

# Madison - Madison - Rose City Dodgers - False - True

#string will have "hello" because is a string assignment while the second line  wont work because string cannot be changed. 

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
# Write a function average_vowels that takes a list of strings as a parameter and returns the
# average number of vowels occurring in each string in the list, both upper- & lower-cased. 
# No library functions aside from input/output.

# Example function call:
# print(average_vowels(list))
# Outputs: 2
# def average_vowels

'''def average_vowels(list):
    vowels = 'aeiou'
    count = 0
    for i in list:
        for a in vowels.upper():
            count += i.upper().count(a)
            totales = count / count
    return totales
list = ["Zebra", "light saber", "1234 JOYS!"]
print(average_vowels(list))
'''
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________