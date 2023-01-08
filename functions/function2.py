# practicing functions
# by Pedro Echavarria


#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
from math import degrees, factorial, log
import random
import turtle
import os
import re
import sys
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
#__________________________________________________________________________________________________

#((((((((((((( House Boat Drawing Program )))))))))))))#

def body(w,h):
    for i in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def house_boat(w,h):
    body(w, h//2)
    turtle.forward(w //2 - h // 2)
    turtle.left(90)
    turtle.forward(h)
    turtle.right(90)
    body(h, h)
    triangle(h)

def main3():
    turtle.color("black")
    turtle.speed(13)
    house_boat(200,100)
    turtle.penup()
    turtle.back(160)
    turtle.pendown()
    house_boat(150,75)

main3()
turtle.Screen().exitonclick()

#__________________________________________________________________________________________________

#          ((((((((((((((((((((((((Challenge: Word Problem))))))))))))))))))))))))

# Your friend is overwhelmed with the number of candidates running in a local election and is
# undecided on whom to vote for.  Write a program to help him decide. Your friend admires
# experience—at least 5 years—but not too much experience that the candidate is disconnected from
# the American people (no more than 20 years)—and wants a candidate who agrees with him on at least
# 80% of the important issues.  Prompt the user to input the candidate’s number of years of experience
# and the percentage agreement on important issues.  Example runs:

# > python3 vote.py
# Enter the candidate’s years of experience: 1
# What percentage of the issues do you and the candidate agree on? 100
# Do not vote for this candidate

# > python3 vote.py
# Enter the candidate’s years of experience: 5
# On what percentage of the issues do you and the candidate agree? 86
# Vote for this candidate


def vote(experience,agreement_percent):

    if experience >= 21 and agreement_percent >=80:
        
        print("Do not vote for this candidate")
    elif experience >= 5 :
        print("Vote for this candidate")
    else:
        print("Do not vote for this candidate")

def main4():
    experience = eval(input('Enter the candidate’s years of experience: '))
    agreement_percent = eval(input('On what percentage of the issues do you and the candidate agree? '))
    vote(experience,agreement_percent)

main4()
#__________________________________________________________________________________________________


# Draws a cake by calling the_candle and rectangle functions.

def cake_layers(width,height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def the_candle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def cake(width,height):  
    for i in range(1):
        cake_layers(width, height - height // 3)
        cake_layers(width, height)
        cake_layers(width, height // 3)
    turtle.forward(width//2 - height//2)
    the_candle(height)
    
def main5():
    turtle.color("black")
    turtle.speed(13)
    cake(290,100)
    turtle.penup()
    turtle.back(260)
    turtle.pendown()
    cake(145,50)
main5()
# keep the drawing up until a click it to exit.
turtle.Screen().exitonclick() 


#__________________________________________________________________________________________________

# Adds all the even numbers together and return their average using a list.
#Example function call:
# print(average_evens([-2, -3, -4, 0, 1, 2, 3, 4]))
# Outputs: 0



# def main():
#     print()
# main()

#__________________________________________________________________________________________________

# Function that takes a list of numbers as a parameter, adds all the 
# negative even numbers (less than 0 and divisible by 2) and 
# returns their average.

def average_neg_evens(list):
    # aggregators to sum the avg.
    sum = 0
    count = 0
    n = 0
    while n < 4:
        for i in list:
            if i < 0 and i % 2 == 0:
                sum += i
                count += 1
        n += 1
    return  sum / count

def main_6():
    test_input = [0, 1, 2, -2, -3, -4, 3, 4]
    output = -3
    print(average_neg_evens(test_input))
    print('lets see!', average_neg_evens(test_input) == output)

main_6()


#__________________________________________________________________________________________________

# Takes a list of strings and a string letter as parameters and returns
# the number of times this letter occurs both upper- & lower-cased.

def count_letter(list, str):
    occurrence_number = 0
    str = str.lower()
    i = 0 # initializing the loop index variable.
    while i < len(list):
        string = list[i] # how to go from index -> value in list
        occurrence_number += string.lower().count(str)
        i += 1
    return occurrence_number

def main_7():
    list = ["HELLO", "goodbye", "1234 Oooh!"]
    print(count_letter(list,"o"))

main_7()

#__________________________________________________________________________________________________

# Write a function average_vowels that takes a list of strings as a parameter and returns the
# average number of vowels occurring in each string in the list, both upper- & lower-cased. 
# No library functions aside from input/output.

# Example function call:
# print(average_vowels(list))
# Outputs: 2
# def average_vowels

def average_vowels(list):
    vowels = 'aeiou'
    count = 0
    for i in list:
        for a in vowels.upper():
            count += i.upper().count(a)
            totales = count / count
    return totales # type:ignore
list = ["Zebra", "light saber", "1234 JOYS!"]
print(average_vowels(list))

#__________________________________________________________________________________________________

# Given a and b, determine their respective comparison points.

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    count_a = 0
    count_b = 0
    count_b = sum(0 for i in range(len(a)) if a[i] == b[i])
    count_a = sum(0 for i in range(len(a)) if a[i] == b[i])
    count_a = sum(1 for i in range(len(a)) if a[i] > b[i])
    count_b = sum(1 for i in range(len(a)) if a[i] < b[i])
    return count_a , count_b

def main_8():
    print(compareTriplets([5 ,6, 7], [3, 6 ,10]))
if __name__ == '__main__':
    main_8()
