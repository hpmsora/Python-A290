#program 1 - print 0 to 9
n = 10
for i in range(n):
    print(i, end=' ')
print('\n')

#program 2 - print with range
for i in range (7, 89, 5):
    print(i, end=' ')
print('\n')

#program 3 - print with list
pets = ['cat', 'dog', 'fish', 'bird']
for animal in pets:
    print(animal, end=' ')
print('\n')

for i in range(len(pets)):
    print(pets[i], end=' ')
print('\n')

#program 4 - letter count
# takes some text from a user
# displays how long the text is
# (ie., nmber of characters)
text = input("Enter any text: ")
count = 0
for i in list(text):
    count += 1
print(count)

#program 5 forever_hello
def forever_hello():
    '''a greeting service; it repeatly requests the name
    of the user and then greets the user'''

    while True:
        name = input('What is your name?')
        print('Hello {}'.format(name))

#program 6 cities
def cities():
    ls = []
    flag = ''
    while True:
        city = input('Enter city: ')
        if city == flag:
            break
        ls.append(city)
    return ls
print(cities())

#program 7 print list
def printList():
    count = 0
    colors = ["red", "green", "blue", "purple"]
    while count < len(colors):
        print(colors[count])
        count += 1
printList()

#program 8 To-do list
def todo():
    ls = []
    while True:
        text = input('Enter any: ')
        if text == '':
            break
        ls.append(text)
    return ls
print(todo())

#program 9 checking
print('Exercise 3')
def checking():
    while True:
        number = input('Enter number: ')

        if number == 'stop':
            break
        else:
            number = int(number)
            if number > 50:
                print('Greater than 50')
            else:
                print('Less than 50')
checking()

#program 10 sumup
print('Exercise 4')
def sumup():
    sum = 0
    while True:
        number = input('Enter number: ')
        if number == 'stop':
            break
        else:
            number = int(number)
            sum += number
    return sum
print(sumup())
