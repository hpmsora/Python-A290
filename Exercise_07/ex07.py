#Exercise 1
def hello(name):
    print('Welcome, ' + str(name) + ', to Python.')
hello('Malgosia')

#Exercise 2
def unique(myList = [], *text):
    #print(len(myList))                                                       
    myList = set(myList)
    myList = sorted(myList)
    return myList
print(unique(['cat', 'dog', 'ant', 'pig', 'dog', 'emu', 'ant', 'dog']))

#Exercise 3
def rng(ls):
    upper = max(ls)
    lower = min(ls)
    return upper - lower

print(rng([4, 0, 1, -2]))

#Exercise 4
  #My original code
def mashup_(myList=[], *text):
    ls = []
    for i in myList:
        ls.append(i)
    ls = set(ls)
    return ls

  #Helped by classmate
def mashup(ls):
    result = set()
    for n in ls:
        result = result | n
    return result

print(mashup([{1,2}, {3, 4}, {5, 6, 7}]))

#Exercise 5
def acronym(ls):
    ls = ls.split(' ');
    ans = []
    for i in ls:
        ans.append(i[0].upper())
    return ''.join(ans)

print(acronym('Random access memory'))
print(acronym('GNU\'s not UNIX'))
