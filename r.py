#for i in range(5):
#	print(i, end="")

t = 0
for v in range(5):
    num = float(input('Please enter a number: '))
    numer = num ** 2
    t += num
print(numer)
print('Average of the square:', t/numer)
