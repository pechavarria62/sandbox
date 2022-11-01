# practicing functions
# by Pedro Echavarria
#***********************
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
from math import degrees
import random
import turtle
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))



turtle.color("blue")

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()


def pyramid(size):
    for i in range(6):
        turtle.forward(size)
        turtle.left(120)

pyramid(200)
back(150)
pyramid(150)
back(100)
pyramid(100)
back(50)

#__________________________________________________________________________________________________

# A function that takes two parameters and return their sum.
def add(x, y):
    return x + y

sum = add(10 , 5)
# print(sum)

#__________________________________________________________________________________________________

# A function that takes two parameters and return the product.
def multiply(x,y):
    return x * y
multi = multiply(2,3)
# print(multi)

#__________________________________________________________________________________________________

# A function that gets two numbers from the user and print their 
# sum and product by calling the two function above.

num1 = int(input("give me one number please: "))
num2 = int(input("give me another number please: "))
print("sum =", add(num1,num2), "product =", multiply(num1,num2))


#__________________________________________________________________________________________________

# A set of functions that call eachother
def f(x): 
	x = x-1
	return g(x)+1

def g(x):
	return x*2

def h(x):
	if x%2 == 1: # is x odd or even
		return f(x) + x # if x is odd
	else:             
		return f(f(x)) # if x is even

print(h(3)) # 8
print(h(4)) # 13
print(h(5)) # 14

#__________________________________________________________________________________________________

# Write a function, that takes a string text and a single surround character 
# surround as parameters:

num1 = input("give me a name please: ")
num2 = input("give me a character please: ")

def header(text,surround):

    print(surround * (len(text) + 4) )    # display top line
    print(surround, text, surround)		      # display middle line
    print(surround * (len(text) + 4) )	  # display bottom line

header(num1, num2)

#__________________________________________________________________________________________________

# Write a function that takes a number as a parameter and returns whether
# or not it is even. 

num3 = int(input("give me one number please: "))

def is_even(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is NOT! a even number")
is_even(num3)

#__________________________________________________________________________________________________

# function that takes's a rectangle's with and height as parameters and
# prints a width X height rectangle .

w = int(input("Give me a number: "))
h = int(input("Give me another number: "))  # type: ignore

def rectangle(x, y):
    for i in range(y):
        print("*" * x)
rectangle(w,h)

#__________________________________________________________________________________________________

def a(x):
    return b(x - 1) * 2

def b(x):
    return x - 4

def c(x, y):
    if x % 2 == 0:
        return x + 3 * y
    else:
        return x - y

print(c(5, b(8)))
print(c(a(3), b(5)))


#__________________________________________________________________________________________________


# Draw a house.

def roof(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def house(len):
    roof(len)
    square(len)

def main1():
    turtle.speed(3)
    turtle.color('black')
    house(100)
    turtle.color("purple")
    turtle.penup()
    turtle.forward(130)
    turtle.pendown()
    house(70)

main1()
turtle.Screen().exitonclick()

#__________________________________________________________________________________________________
#((((((((((((( drawing )))))))))))))#
# a Stop Sign wi wu wi wu!!!

def post(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def octagon(len):
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)
        


def stop(len):
    octagon(len)
    turtle.forward(3/8 * len)
    post(1/5 * len, 2 * len)

def main2():
    turtle.speed(1)
    turtle.color("blue")
    stop(20)
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    turtle.color("green")
    stop(50)
main2()
turtle.Screen().exitonclick()

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

import turtle

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

list = ['Zebra', 'lightsaber', '1234 JOYS!']
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
        total = contar.count("0") # type: ignore
    else:
        print("You entered", total, "Zeros")# type: ignore
        break

#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
#__________________________________________________________________________________________________
