#Program 1
def char_count(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()

    return len(wordList)

#print(char_count('poem.txt'))

print("\n")

#Exercise 1
def len_str(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    return len(content)

print("Length of string")
print("100worst.txt:\t" + str(len_str('100worst.txt')))
print("abacus.txt:\t" + str(len_str('abacus.txt')))
print("\n")

def len_word(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    return len(wordList)

print("Length of words")
print("100worst.txt:\t" + str(len_word('100worst.txt')))
print("abacus.txt:\t" + str(len_word('abacus.txt')))
print("\n")

def len_line(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split('\n')
    return len(wordList)

print("Length of lines")
print("100worst.txt:\t" + str(len_line('100worst.txt')))
print("abacus.txt:\t" + str(len_line('abacus.txt')))
print("\n")
