import os
from nltk.corpus import stopwords
import operator

# * file operations
    # need to find and open my file for reading
    # also writing output to a file we designate
def openFile(name):
    contents = open(name,'r')
    subject = contents.read()
    return subject

content = openFile("trump.txt")

# * word accumlation
    # consider how to store the wordcount
    # we could use lists, tuples, dictionaries...
    # choosing dictionaries because of their efficient structure
def countingWords(contents):
    words = contents.split(' ')
    word_dict = dict()
    for word in words:
        if not word in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

countingWords(content)

# * undesirable noise & words
    # puncuation, special characters
    # stopwords (ie., pronouns, definite articles, etc.)
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
def desirableCountingWords(contents):
    words = contents.split(' ')
    word_dict = dict()
    for i in stopwords:
        word_dict[i] = 0
    for word in words:
        if word in stopwords:
            word_dict[word] += 1
    return word_dict

desirableCountingWords(content)

# * word uniqueness
    # maybe check using .lower()
def uniquenessWords(contents):
    words = contents.split(' ')
    wording = []
    for word in words:
        if not word.lower() in wording:
            wording.append(word.lower())
    return wording

print(uniquenessWords(content))

# * sorting
    # dictionaries are not a sequence
    # since if given a key, we can return a value;
    # and if given a value, we can return a key;
    # (but we have no way to 'guess' the values);
    # we need a way to sort on values
    # (to get top n)
    # how to do it?
    
    # use itemgetter() of class operator to accomplish this
    # syntax is sorted(iterable, key=None, reverse=False)
    # key = operator.itemgetter(1)
    
############
    # ALGORITHM

# * import packages
# * declare variables
    # my_dict ={}
    # stop = stopwords
            # ** BTW: to reduce list traversal time on stopwords
            # consider converting stopwords to hashable type set
            
