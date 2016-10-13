# Won Yong Ha
#
# 13 October 2016
#
# Final Exam

print("")

# 1

def Easy_1(listOfWords):
    newIntList = []
    for i in listOfWords:
        newIntList.append(len(i))
    return newIntList

print("Easy 1")
print(Easy_1(["hello","morning","available", "tea","fantastic"]))
print("")

# 2

def Easy_2(listOfWords):
    newWordsList = []
    avg = 0
    for i in listOfWords:
        avg += len(i)
    avg /= len(listOfWords)
    for i in listOfWords:
        if len(i) < avg:
            newWordsList.append(i)
    return newWordsList

print("Easy 2")
print(Easy_2(["hello","morning","available", "tea","fantastic"]))
print("")

# 3
def Medium_1(fileName):
    newLineList = []
    count = 0
    context = open(fileName, 'r')
    context = context.read().split('\n')
    for i in context:
        count += 1
        if 'Make America Great Again' in i:
            print(i + "    " + str(count))

print("Medium 1")
Medium_1('trump.txt')
print("")

# 4
def Hard_1(listOfStrings):
    newBoolList = []
    for i in listOfStrings:
        newString = ''
        for j in list(i):
            if j.isalpha():
                newString += j
        newString = newString.lower()
        newReverseString = Reversed(newString)
        if newReverseString == newString:
            newBoolList.append(True)
        else:
            newBoolList.append(False)
    return newBoolList

def Reversed(word):
    newString = ''
    count = len(word) - 1
    while count >= 0:
        newString += list(word)[count]
        count -= 1
    return newString

print("Hard 1")
print(Hard_1(["A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!","A Toyota! Race fast, safe car! A Toyota!", "You are too early for the meeting","Are we not drawn onward to new era?","A nut for a jar of tuna.","This is not a good choice of questions!"]))
print("")
