#for loop
#sequence with a string

name = 'Apple'
for ch in name:
    print(ch)


#for loop
#sequence with a list

for word in ['stop', 'desktop', 'post', 'top']:
    if 'top' in word:
         print(word)

print('Done.')


#for loop with range

for i in range(4):
    print(i)
# 0, 1, 2, 3

for i in range(3, 6):
    print(i)
# 3, 4, 5

for i in range(3, 8, 2):
    print(i)
# 3, 5, 7
print('\n')

#Exercise 1 for loop
# a
print('a')
for i in range(11):
    print(i)
print('\n')

# b
print('b')
for i in range(1, 10):
    print(i)
print('\n')

# c
print('c')
for i in range(0, 9, 2):
    print(i)
print('\n')

# d
print('d')
for i in range(1, 10, 2):
    print(i)
print('\n')

# e
print('e')
for i in range(20, 61, 10):
    print(i)
print('\n')

# f
print('f')
for i in range(1, 6):
    print(i*-100)
print('\n')

# g
print('g')
for i in range(-10, 11, 2):
    print(i)
print('\n')


#Lecture Note
for fruit in ['pear', 'apple', 'peach', 'plum']:
    print(fruit.upper());
print('\n')

fruits = []
for fruit in ['pear', 'apple', 'peach', 'plum']:
    fruits.append(fruit.upper())
print(fruits)
print('\n')

n = 10
for i in range(n):
    print(i, end=' ')
print('\n')

pets = ['cat', 'dog', 'fish', 'bird']
for animal in pets:
    print(animal, end=' ')
# cat dog fish bird

for i in range(len(pets)):
    print(pets[i], end=' ')
# cat dog fish bird


#Exercise 2 - for loops
# a
print('a')
for ch in 'test':
    print(ch, end=' ')
print('\n')

# b
print('b')
colors = ['red', 'blue', 'green']
for color in colors:
    print(color, end=' ')
print('\n')

# c
print('c')
li = ['a', 'b', 'c', 'd', 'e']
for i in li:
    print(i + ': ' + str(li.index(i)), end=', ')
print('\n')

# d
print('d')
word = 'coding'
for i in range(len(word)):
    print(i, word[i])
print('\n')
