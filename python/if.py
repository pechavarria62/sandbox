# ifs statements snippets 
# by Pedro Echavarria


# Program that ask the user for the current temperature and 
# output what they should wear.

temp = eval(input("What's the tempereture outside today?:  "))
if temp > 90:
	print("Whoa, it's boiling!")
elif temp >= 80:
	print("it's getting hot")
elif temp >= 60:
	print("A perfect day")
elif temp >= 32:
	print("Don't forget your sweater")
else:
	print("Brrr, you need a coat")


###########################################################################

# this program output what time to wake up depending of the
# day and the weather conditions\

DoW = input("Enter a day: ")

if DoW == "Saturday":
	print("Wake up at 9 am")
elif DoW == "Sunday":
	print("Wake up at 10 am")
else:
	print("Wake up at 7 am")

###########################################################################

# A program that takes a number from 0-100 as input and print the
# equivalent string letter grade. (no +/-)
grade = eval(input("Please enter a grade from 0-100: "))

if grade >= 90:
	print("A")
elif grade >= 80:
	print("B")
elif grade >= 70:
	print("C")
elif grade >= 60:
	print("D")
else:
	print("F")

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################



