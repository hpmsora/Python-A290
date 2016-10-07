# Won Yong Ha
# Exercise 13

#exercise 1
def listComprehension1(contents):
    words = contents.split()
    word_length = []
    for word in words:
        if word != "the":
            word_length.append(len(word))
    return word_length

print("Exercise 1")
print(listComprehension1("the quick brown fox jumps over the lazy dog"))
print("\n")

#exercise 2
def listComprehension2(contents):
    new_list = []
    for i in contents:
        if i >= 0:
            new_list.append(i)
    return new_list

print("Exercise 2")
print(listComprehension2([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]))
print("\n")

#exercise 3
def listComprehension3(ls1, ls2):
    new_list = []
    for i in ls1:
        for j in ls2:
            new_list.append((i, j))
    return new_list

print("Exercise 3")
print(listComprehension3(["red", "green", "yellow", "blue"], ["flowers", "copies", "snakes"]))
print("\n")

#exercise 4
def listComprehension4(num):
    new_list = []
    for i in range(1, num):
        for j in range(i, num):
            for k in range(j, num):
                if i*i + j*j == k*k:
                    new_list.append((i, j, k))
    return new_list

print("Exercise 4")
print(listComprehension4(30))
print("\n")

#exercise 5
def join1(contents):
    return "|".join(contents)

print("Exercise 5")
print(join1(["This", "is", "a", "delimited", "string"]))
print("\n")

#exercise 6
def join2(contents, junk):
    new_list = []
    for item in contents:
        for i in reversed(range(len(junk) + 1)):
            new_junk = junk[0:i]
            item = item.replace(new_junk, "")
        new_list.append(item)
    return new_list

print("Exercise 6")
print(join2(['40.70636; -74.00709</', '40.2177; -74.7637</sp', '40.961051; -74.29448<', '39.947; -75.145</span'], "</span>"))
