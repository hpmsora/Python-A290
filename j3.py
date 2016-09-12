#Exercise 1
def word_freq():
    text = input("Enter text: ")
    ls = text.split( )
    ls_ans = set(ls)
    
    for i in ls_ans:
        count = 0;
        for j in ls:
            if j == i:
                count += 1
                ans_str = str(i) + "\tappears " + str(count) + " times."
                print(ans_str)
word_freq()

#Exercise 2
def unique(myList = [], *text):
    #print(len(myList))
    myList = set(myList)
    myList = sorted(myList)
    print(myList)
unique(['cat', 'dog', 'ant', 'pig', 'dog', 'emu', 'ant', 'dog'])

#Exercise 3
def mashup(myList=[], *text):
    ls = []
    for i in myList:
        ls += i
    print(ls)
mashup([{1,2}, {3, 4}, {5, 6, 7}])

#Exercise 4
def count_singles(myList=[], *text):
    ls = []
    for i in myList:
        ls += i
    s_ls = set(ls)
    ls_anw = []
    count = 0
    for x in s_ls:
        for i in ls:
            if x == i:
                count += 1
        print(str(x) + " "+ str(count))
        if count == 1:
            print(str(x))
            ls_anw += [x]
        count = 0
    print(len(ls_anw))
count_singles([[2,0,3], [2,1,4], [3,5,0]])
