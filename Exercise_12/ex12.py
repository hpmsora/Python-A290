# Won Yong Ha
# EX12

from urllib.request import urlopen
from html.parser import HTMLParser

#Exercise 1

print("Exercise 1\n")

def news(url, wordsList):
    infile = urlopen(url)
    contents = infile.read()
    contents = contents.decode()
    wordsDict = dict()
    for word in wordsList:
        count = contents.count(word)
        wordsDict[word] = count
    print(wordsDict)

news('http://bbc.co.uk', ['economy', 'climate', 'education'])
print("\n")

#Exercise 2

print("Exercise 2\n")

#Helped by Timi Liu
# Source and helped from Google too
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0
    def handle_starttag(self, tag, attrs):
        if tag not in {'br','p'}:
            print('{}{} start'.format(self.indent*' ', tag))
            self.indent += 4
    def handle_endtag(self, tag):
        if tag not in {'br','p'}:
            self.indent -= 4
            print('{}{} end'.format(self.indent*' ', tag))

def parsering(url):
    infile = open(url)
    content = infile.read()
    infile.close()
    myparser = MyHTMLParser()
    myparser.feed(content)

parsering('w3c.html')

print("\n")
