#Multiplication table

import random

#Homework 1 - 1
for i in range(1, 11):
    for j in range (1, 11):
        print(str(i * j), end='\t')
    print("\n")
print('\n')

#Homework 1 - 2
def hw1_2():
    ans = random.randrange(100)
    attempts = 0

    while True:
        attempts += 1
        i = input('Your guess?: ')
        i = int(i)
        if i == ans:
            print('Correct!')
            print('You tried ' + str(attempts) + ' times')
            break
        elif i > ans:
            print('Lower')
        else:
            print('Higher')

hw1_2()
