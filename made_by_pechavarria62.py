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

def output_stats(list,another):
    print("Mean: ", statistics.mean(list), statistics.mean(another),sep=" "*5)
    print("Median: ", statistics.median(list), statistics.mean(another),sep=" "*5)
    print("STD:    ", statistics.stdev(list), statistics.mean(another),sep=" "*5)
    print()

spring = []
fall = []
data = "sample_grades.csv"
file = open(data)
for line in file:
    list = line.rstrip().split(",")
    
    if list[1] == 'Spring 2016':
        spring.append(eval(list[2]))  
    else:
        fall.append(eval(list[2]))  

file.close()
def main():
    print('','Fall 2016: ', 'Spring 2016:', sep=" "*10)
    output_stats(fall,spring)
main()
