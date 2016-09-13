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
unique(['cat', 'dog', 'ant', 'pig', 'dog', 'emu', 'ant', 'dog'])

def acronym(ls):
    return ls[0] + ls[1] + ls[2]
