# (((((((((((((((((((((( by Pedro Echavarria ))))))))))))))))))))))

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

from math import factorial, log
import turtle
import random
import statistics

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

# Program reads in a csv file and outputs the mean, median, and standard deviation for
# the fall & spring semesters.

def output_stats(list,easter):
    mms = ['Mean  ','Median','STD    ']
    mean_fall = "%.2f" % statistics.mean(list) 
    mean_spring = "%.2f" % statistics.mean(easter)

    median_fall = "%.2f" % statistics.median(list) 
    median_spring = "%.2f" % statistics.median(easter)

    std_fall = "%.2f" % statistics.stdev(list) 
    std_spring = "%.2f" % statistics.stdev(easter)

    print(' '*10,'Fall 2016', 'Spring 2016',sep=" "*5 )
    print(mms[0],mean_fall,mean_spring,sep="  "*5)
    print(mms[1],median_fall,median_spring ,sep="  "*5)
    print(mms[2],std_fall,std_spring,sep="  "*5)

spring = []
fall = []
data = "sample_grades.csv"
def sort_csv():
    file = open(data)
    for line in file:
        list = line.rstrip().split(",")
        
        if list[1] == 'Spring 2016':
            spring.append(eval(list[2]))  
        else:
            fall.append(eval(list[2]))  
    file.close()

def main():
    sort_csv()
    output_stats(fall,spring)
main()
