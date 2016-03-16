# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:19:09 2016

@author: jonathandeng
"""
def readText(path):
    #open file to check
    file = open(path, 'r')
    contents = file.read()
    return str(contents)
    file.close()

def purgoMalum(text):
    import urllib
    purger = 'http://www.purgomalum.com/service/containsprofanity?text='
    urlcheck = purger + text
    output = urllib.urlopen(urlcheck).read()
    print output
    

text = readText('/Users/jonathandeng/Downloads/movie_quotes.txt')
purgoMalum(text)