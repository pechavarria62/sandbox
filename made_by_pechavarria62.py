# (((((((((((((((((((((( by Pedro Echavarria ))))))))))))))))))))))

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

from math import factorial, log
import turtle
import random

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

# Program that asks the user for their favorite month and day of the month as input and outputs
# The month & day followed by the year, Whether or not the month is alphanumeric, The number of
# 2’s in the number The factorial of the number and The log base 2 of the absolute value of the number.

def day():
    favorite_month = input("Please enter your favorite month: ")
    favorite_day = input("Enter your favorite day of the month: ")
    str1 = favorite_month[0].upper()
    str2 = favorite_month[1:].lower()
    print(str1 + str2, favorite_day , ", 2020")
    print("Is the month alphanumeric?", favorite_month .isalnum())
    print("How many 2’s?",favorite_day.count("2"))
    favorite_day = int(favorite_day)
    print("Factorial: ", factorial(favorite_day)) 
    print("Log base 2: ", log(abs(favorite_day), 2)) 

day()