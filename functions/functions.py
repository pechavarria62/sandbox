# practicing functions
# by Pedro Echavarria
#***********************
#((((((((((((((((((((((((( Imports )))))))))))))))))))))))))
from math import degrees, factorial, log
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

# A set of functions that call each other
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
