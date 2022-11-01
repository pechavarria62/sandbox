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

def count_fricatives(list):
    fricative = 'fsvz'
    count = 0
    for i in list:
        for consonants in fricative.upper():
            count += i.upper().count(consonants)
    return count

list = ['Zebra', 'lightsaber', '1234 JOYS!']
print(count_fricatives(list))
print(count_fricatives(list) == 3)


#__________________________________________________________________________________________________




#__________________________________________________________________________________________________


#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________