# Writing programs by Pedro Echavarria

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

from math import factorial, log
import turtle
import random
import statistics
import os

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

# __________________________________________________________________________________________________

# Create a list of 20 numbers input by the user and print the average(mean)of the list.


def average_num():
    list = []
    for i in range(20):
        num = int(input("give me a number: "))  # type: ignore
        list.append(num)

    return sum(list)/len(list)


print("the average is ", average_num())


# __________________________________________________________________________________________________

# Function (mangle) that takes a string as a parameter and returns the string after performing the following operations:

# Converting the string to all upper case letters
# Removing the third character
# Removing the third to last character

# Example function calls:	                      Output:
# print(mangle(“hellothere”))	                 HELOTHRE
# print(mangle(“42 degrees Celsius”))	        42DEGREES CELSUS
# print(mangle(“eeeeeee”))	                        EEEEE


def mangle(str):
    str = str.upper()
    str = str[0:2] + str[3:-3] + str[-2:]
    return str


def main1():
    print(mangle("hellothere"))
    # Test mangle
    test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    test_output = ['HELOTHRE', '42DEGREES CELSUS', 'EEEEE']
    for i in range(len(test_input)):
        print('Mangle', test_input[i] + ':',
            mangle(test_input[i]) == test_output[i])


main1()


# __________________________________________________________________________________________________

# Write a function, that takes a list of strings as a parameter and returns the total
# number of upper and lower case e’s (“E” and “e”) in all the strings in the list. Test that your
# function works with multiple examples.


# Example function call:	Output:
# print(count_e([“hi”, “hello”, “EEK!”]))	3

def count_e(list):
    num_e = 0  # sum -- aggregates values
    for string in list:
        num_e += string.upper().count("E")
    return num_e


def main2():
    # Test count_e
    print(count_e(["hi", "hello", "EEK!"]))
    print("count_e", count_e(["hi", "hello", "EEK!"]) == 3)


main2()
# __________________________________________________________________________________________________

# Write a function,that takes a list of strings as a parameter and returns the
# total number of upper and lower case vowels (A, E, I, O, U) in all the strings in the list.

# Example function call:	Output:
# print(count_vowels([“hi”, “hello”, “OOF!”]))	5


def count_vowels(list):
    num_vowels = 0  # sum -- aggregates values
    for string in list:
        upper = string.upper()
        for vowel in "AEIUO":
            num_vowels += upper.count(vowel)

    return num_vowels


def main3():
    # Test count_e
    print(count_vowels(["hi", "hello", "OOK!"]))
    print("count_e", count_vowels(["hi", "hello", "OOK!"]) == 5)


main3()
# __________________________________________________________________________________________________

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

# > python vote.py
# Enter the candidate’s years of experience: 21
# On what percentage of the issues do you and the candidate agree? 90
# Do not vote for this candidate

# > python vote.py
# Enter the candidate’s years of experience: 20
# On what percentage of the issues do you and the candidate agree? 80
# Vote for this candidate


def vote(experience, agreement_percent):

    if experience >= 21 and agreement_percent >= 80:

        print("Do not vote for this candidate")
    elif experience >= 5:
        print("Vote for this candidate")
    else:
        print("Do not vote for this candidate")


def main4():
    experience = eval(input('Enter the candidate’s years of experience: '))
    agreement_percent = eval(
        input('On what percentage of the issues do you and the candidate agree? '))
    vote(experience, agreement_percent)


main4()


# __________________________________________________________________________________________________

# Program reads in a csv file and outputs the mean, median, and standard deviation for
# the fall & spring semesters.

def output_stats(list, easter):
    mms = ['Mean  ', 'Median', 'STD    ']
    mean_fall = "%.2f" % statistics.mean(list)
    mean_spring = "%.2f" % statistics.mean(easter)

    median_fall = "%.2f" % statistics.median(list)
    median_spring = "%.2f" % statistics.median(easter)

    std_fall = "%.2f" % statistics.stdev(list)
    std_spring = "%.2f" % statistics.stdev(easter)

    print(' '*10, 'Fall 2016', 'Spring 2016', sep=" "*5)
    print(mms[0], mean_fall, mean_spring, sep="  "*5)
    print(mms[1], median_fall, median_spring, sep="  "*5)
    print(mms[2], std_fall, std_spring, sep="  "*5)


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


def main5():
    sort_csv()
    output_stats(fall, spring)


main5()


# __________________________________________________________________________________________________

# Reverse an array
def reverseArray(a):
    b = len(a)-1
    return a[b::-1]


def main6():
    arr = [1, 4, 3, 2]
    print(reverseArray(arr))


main6()

# __________________________________________________________________________________________________

# Program prints out the files and folders names you have in path.

# imput_path = input("Enter path please: ")
# FOLDER_PATH =  r"imput_path"
FOLDER_PATH = r"/Volumes/personal/repos/sandbox"  # files path.


def listDir(dir):
    filesNames = os.listdir(dir)
    for filesName in filesNames:
        print('File Name ' + filesName)


if __name__ == '__main__':
    listDir(FOLDER_PATH)
# -------------------------------------------------------
# Example Output:
# File Name hello.py
# File Name texts_files
# File Name ._.vscode
# File Name if.py
# File Name ForLoops.py
# File Name try.py
# File Name fors_ifs.py
# File Name functions.py
# File Name programs.py
# File Name hard-drive-read.py

# __________________________________________________________________________________________________

# Store lines of a file into array/list Print out the first & last two
# elements of the array/list, and the number of lines

files = "texts_files/turing.txt"
array = []

def turing():
    # Open the file and append it to the empty array.
    with open(files) as f:
        array = [x.rstrip() for x in f.readlines() if len(x.rstrip()) != 0]
        f.close()
    # Take the first & last two elements.
    array = array[0:-2]
    # count the amount of line in the array
    num_lines = sum(1 for line in array)
    return array, 'number of line',num_lines

def main():

    print(turing())
    
main()
#__________________________________________________________________________________________________

# output:

# (['The Imitation Game (2014)', "Based on the real life story of legendary
# cryptanalyst Alan Turing, the film portrays the nail-biting race against time
# by Turing and his brilliant team of code-breakers at Britain's top-secret
# Government Code and Cypher School at Bletchley Park, during the darkest days
# of World War II.", 'The true enigma was the man who cracked the code'],
# 'number of line', 3)


# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
