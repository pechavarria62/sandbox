
# Writing Loops
# by Pedro Echavarria

# (((((((((((((((((((((((((( Imports ))))))))))))))))))))))))))

import turtle

# (((((((((((((((((((((((((( Imports ))))))))))))))))))))))))))

# print numbers form 1 up to but including 6.
for a in range(1,6):
    print(a)
print('_'*20)
print()

#__________________________________________________________________________________________________

# print numbers form 2 up to but including 12 in steps of 3.
for b in range(2,12,3):
    print(b)
print('_'*20)
print()

#__________________________________________________________________________________________________
# Print **** 4 times.
for c in range(4):
    print("****") 
print('_'*20)
print()

#__________________________________________________________________________________________________

# Print a triangle.
turtle.color("blue")
size = 100
# Repeat 3 times
for d in range(3):
    turtle.forward(size)
    turtle.right(120)

print('_'*20)
print()

#__________________________________________________________________________________________________

for e in "hello":
    print(e)
print('_'*20)
print()

#__________________________________________________________________________________________________

for f in range(4):
    print(f)
print('_'*20)
print()

#__________________________________________________________________________________________________

for h in "CSCI 150":
    print(h)
print('_'*20)
print()

#__________________________________________________________________________________________________

for j in range(-10, 1, 2):
    print(j, end=" ")
print()
print('_'*20)
print()

#__________________________________________________________________________________________________

# Print numbers from 10 up to but not including 30 in steps of 5.
for k in range(10, 30, 5):
    print(k, end=" ")
print()
print('_'*20)
print()

#__________________________________________________________________________________________________


# print the average of 10 real(decimal) numbers.
# Average is the sum of number divided by the amount of numbers. 

s = 0 # This is called Aggregator variable and must be initialized before the loop. 
for l in range(10):
    num = eval(input('Enter your real # dude: '))
    s += num // 10
print('The Average number is: ', s )

print('_'*20)
print()

#__________________________________________________________________________________________________

# Print numbers from 10 down to but not including -25 in steps of -5.
for m in range(10, -25, -5):
    print(m, end=" ")
print('_'*20)
print()

#__________________________________________________________________________________________________

# Print numbers from -3 up to but not including 21 in steps of 3.
for n in range(-3, 21, 3):
    print(n, end=", ")
print()
print('_'*20)

#__________________________________________________________________________________________________
t=1
print(0, end=" " )
for ?? in range(5):
    print(t, end=' ')
    t *=4
print('_'*20)
print()
#__________________________________________________________________________________________________

string = 'GOODBYE' 
for q in string:
    print(q, end="-")
print("!")
print('_'*20)
print()
#__________________________________________________________________________________________________

# Ask user for 3 team names and print Go 
# team name! for each team
#

for r in range(3):
    teams = input('Please enter a team name: ').upper()
    print('GO... ', teams + "!")  # type: ignore
print('_'*20)
print()

#__________________________________________________________________________________________________

# Ask user for 5 number and returns the square of the average number.

sq = 0
for s in range(5):
    num = eval(input("Please enter a number: "))
    sq += num ** 2 / 5
print("Average of the squares: ", sq)
print('_'*20)
print()
#__________________________________________________________________________________________________

# Write content in a file from a user.
prompt = "Insert your letter: "
outFileName = input('What is the name of your output file?: ')
num_lines  = eval(input('how many line do you want to write?: '))

# Create a new file object , in "write" mode.
dataFile = open(outFileName, 'w') # use (a) to append.
for x in range(num_lines):
    userInput = input(prompt)
    # write the user input in the file.
    print(userInput, file=(dataFile))

dataFile.close()

#__________________________________________________________________________________________________

# Open a file and display its content/data.

files = open("yeas.txt")
for i in files:
    print(i.rstrip())
files.close()

#__________________________________________________________________________________________________

# Count the number of letters grades in a file.
letters = ['A','B','C','D','F','G','M','H','Q']
count = {}
file = "yeas.txt"
# loop through all line in file.
for line in open(file):
    letter = line.replace('\n', '').upper() # if any form of space like comas (,) replace them.
    # get the amount of letter if they exist if not return 0
    counts = count.get(letter, 0)  # type: ignore
    # store count
    count[letter] = counts + 1  # store count

# print out count.
print("Letter count: ")
for l in letters:
    print(l + ':', count.get(l, 0))
print()
print('-'* 20)
print()

print("File Grades Count")

for item in count.keys():
    print(item + ':', count[item])

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
#__________________________________________________________________________________________________