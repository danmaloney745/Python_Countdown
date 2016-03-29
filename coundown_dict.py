#Daniel Maloney
#G00303381

#Import the time and random packages for timing how the program runs, and for randomising the anagram.
import random
import time
start_time = time.time()

#Readin from the file, populate a list with the contents of the file.
with open('sorted_words.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

#Define arrays to hold the consonants and vowels
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

#Three loops to satisfy the condition of having a set number of consontants and vowels, the third loop pulls from either a consonant or a vowel
def get_anagram():
    anagram = []
    for i in range (0,3):
        anagram.append(random.choice(vowels))
    for i in range (0,4):
        anagram.append(random.choice(consonant))
    for i in range (0,2):
        anagram.append(random.choice(vowels + consonant))
    return anagram

# Imports the shuffle function and shuffles the anagram
def sort_anagram(anagram):
    sorted_ana = [(''.join(sorted(anagram)))]
    return sorted_ana

#Taking a look at different types of data structures in python, came accross dictionaries which work allow for the assignment of keys and values, with experience with maps in java I should be able to search the dictionary for key values, thus improving the search time for the anagram values.
#http://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python
from collections import defaultdict

#Method to join the words list with a new list of keys, using dict(zip()) I can then join the two lists into one dictionary.
def get_dict():
    keys = []
    for e in words:
        keys += [''.join(sorted(e))]
    newdict = dict(zip(keys, words))
    return newdict


#anagram = get_anagram()
anagram = ['s','t','r','e','a','m','i','n','g']

#Sort the anagram into a string, and also assign the dictionary.
sortedanagram = (''.join(sort_anagram(anagram)))
anadict = get_dict()

#Using the code excerpt below I was able to compare the dictionary keys for the sorted anagram.
#http://stackoverflow.com/questions/10795973/python-dictionary-search-values-for-keys-using-regular-expression
def search(dictionary, anagram):
    result = []
    for key in dictionary:
        if anagram in key:
            result.append((key, dictionary[key]))
    return result

#print and search the dictionary for the anagram values.
print(search(anadict, sortedanagram))


print("--- %s seconds ---" % (time.time() - start_time))
