# (((((((((((((((((((((( by Pedro Echavarria ))))))))))))))))))))))

#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

from math import factorial, log
import turtle
import random
import statistics
import os


#  ((((((((((((((((((((((((((( Imports )))))))))))))))))))))))))))

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
