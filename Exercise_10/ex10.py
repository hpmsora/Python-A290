#WonYong Ha (woha)
#Collaborate with Yanlin Liu, usename:yanlliu

from collections import defaultdict

#Exercise 1
print("\n")
print("Exercise 1")
def arithmetic(ls):
    if len(ls) <= 2:
        return True
    diff = ls[1] - ls[0]
    for i in range(len(ls) - 1):
        if not (ls[i + 1] - ls[i] == diff):
            return False
    return True

print(arithmetic([]))
print(arithmetic([3]))
print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3, 6, 9, 11, 14]))
print("\n")

#Exercise 2
print("Exercise 2")

ls = list('abcdefgh')
print(ls[-1:1])
print(ls[:4])
print(ls[3:6])
print(ls[3:4])
print(ls[-3:-2])
print(ls[3:])
print(ls[5:])
print("\n")

#Exercise 3
events = '5/14 2:30 PM\n5/15 11:15 AM\n5/15 1:00 PM\n5/16 9:00 PM'
events_frag = events.split()

 # a
count = 0

print("Exercise 3 - a")
for i in  events_frag:
    if i == '5/15':
        count += 1
print("5/15: " + str(count))

events_order = events.split('\n')
events_ordering = []
for i in events_order:
    events_ordering.append(i.split())
print("\n")

 # b
count = 0

print("Exercise 3 - b")
for i in events_ordering:
    if i[0] == '5/15':
        print("Start: " + str(count), end = ' ')
    for j in i:
        count = count + len(j) + 1
    if i[0] == '5/15':
        print("End: " + str(count))
        break
    count += 2
print("\n")

 #c
count_word = 0
flag = 0
flagCurr = 0
flagPre = 0
end = 0

print("Exercise 3 - c")
for i in events_ordering:
    if i[0] == "5/15":
        flagCurr = 1
    else:
        flagCurr = 0

    tempCount = 0
    for j in i:
        tempCount = tempCount + len(j) + 1
    tempCount += 1
    
    if flag == 1 and not (flagCurr == flagPre):
        print("Start: " + str(count_word), end = ' ')
        print("End: " + str(count_word + tempCount))
        break
    count_word += tempCount
    flagPre = flagCurr
    if i[0] == "5/15":
        flag = 1

print("\n")

 #d
st = ""

print("Exercise 3 - d")
for i in events_ordering:
    if i[0] == "5/15":
        for j in i:
            st = st + j + " "
        print(st)
        st = ""
print("\n")

#Exercise 4
def lookup(ls):
    while(True):
        print("\'exit' for escape")
        firstName = input("Enter the first name: ")
        if firstName == 'exit' or firstName == 'Exit':
            break
        lastName = input("Enter the last name: ")
        if lastName == 'exit' or lastName == 'Exit':
            break
        key = (firstName, lastName)
        ls = defaultdict(lambda: "The name you entered is unknown", ls)
        print(ls[key])

phonebook = {
    ('Anna', 'Karenina'): '(123) 456-7890',
    ('Yu', 'Tsun'): '(901) 234-5678',
    ('Hans', 'Castorp'): '(321) 908-7654'}

lookup(phonebook)
print("\n")

#Exercise 5

 # a
print("Exercise 5 - a")
def isNumber(num):
    try:
        val = int(num)
        print("Success")
    except ValueError:
        print("Error - Not a Number")

x = input("Enter number: ")
isNumber(x)
print("\n")

 # b
print("Exercise 5 - b")
def search(ls, num):
    try:
        val = ls[num]
        print("Success")
    except IndexError:
        print("Error - non-existent")

exampleList = [1, 2, 3, 4, 5, 6, 7]
print(exampleList)
print("\n")
print("Input: 1")
search(exampleList, 1)
print("Input: 8")
search(exampleList, 8)
print("Input: 9")
search(exampleList, 9)
print("\n")

 # c
print("Exercise 5 - c")
def divide(x, y):
    try:
        val = x / y;
        print("Success")
        print("Result Value: " + str(val))
    except ZeroDivisionError:
        print("Error - Divided by 0")

print("x: 2, y: 1 -> ", end = ' ')
divide(2, 1)
print("x: 2, y: 0 -> ", end  = ' ')
divide(2, 0)
print("\n")
