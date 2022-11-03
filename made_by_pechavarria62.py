# (((((((((((((((((((((( by Pedro Echavarria ))))))))))))))))))))))

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

from math import factorial, log
import turtle
import random
import statistics

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

# Program reads in a csv file and outputs the mean, median, and standard deviation for
# the fall & spring semesters. 

# Make sure to write at least two functions in your final solution. The more generalizable
# you make your code, the more you may be able to reuse it for your own project later. To
# receive feedback, please submit a screenshot of your program & its output.

data = "sample_grades.csv"
spring = ()
fall = ()
file = open(data)
for line in file:
    print(line.rstrip())

file.close()