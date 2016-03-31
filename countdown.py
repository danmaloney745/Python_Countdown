#Import the time and random packages for timing how the program runs, and for randomising the anagram.
import random

#Readin from the file, populate a list with the contents of the file.
with open('scrabble_words.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

#Define an array to hold the anagram, additional arrays hold the consonants and vowels

vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

#Three loops to satisfy the condition of having a set number of consontants and vowels, the third loop pulls from either a consonant or a vowel.

def get_anagram():
    anagram = []
    for i in range (0,3):
        anagram.append(random.choice(vowels))
    for i in range (0,4):
        anagram.append(random.choice(consonant))
    for i in range (0,2):
        anagram.append(random.choice(vowels + consonant))
    return anagram
    
#Sort the anagram, for improved searching and comparisson
#Also prints the anagram

from random import shuffle
def sort_anagram(anagram):
    shuffle(anagram)
    print (''.join(anagram))
    sorted_ana = [(''.join(sorted(anagram)))]
    return sorted_ana


#First atempt of permuatating every sequence of the anagram. Runs horribly slow and can use some optimisation.

#def perm1(lst):
#    if len(lst) == 0:
#        return []
#    elif len(lst) == 1:
#        return [lst]
#    else:
#        anaPerm = []
#        for i in range(len(lst)):
#            pos = lst[i]
#            xs = lst[:i] + lst[i+1:]
#            for p in perm1(xs):
#                anaPerm.append([pos]+p)
#        return anaPerm   

#perm2 is a little faster than the previous permutation method (making use of the yield keyword), but still falls apart when checking an anagram of size 9.

#def perm2(lst):
#    if len(lst) == 0:
#        yield []
#    elif len(lst) == 1:
#        yield lst
#    else:
#        anaPerm = []
#        for i in range(len(lst)):
#            pos = lst[i]
#            xs = lst[:i] + lst[i+1:]
#            for p in perm1(xs):
#                anaPerm = yield [pos]+p
#        return anaPerm
    
#Simple compare method that comapares two lists to see if the dictionary (sorted_words) contains the anagram. The compare method is fine with anagrams of small size, but with an anagram of 9 letters it took some time to complete.

#def comp(list1, list2):
#    compAna = []
#    for word in list1:
#        comp = ''.join(sorted(word))
#        if comp in list2:
#            if (len(word) > 2):
#                compAna.append(word)
#                break;
#            else:
#                continue
#    return compAna

#Decided to check different types of comparing lists, as the comparisson method I had created was really bogging the program down. http://bookmarks.honewatson.com/2008/05/28/python-list-compare-difference-python-sets/

#Using the intersection of two lists and the itertools permuatations method really speeds up the program.

def compare_lists(list1, list2):
    return list(set(list1) & set(list2))

#Found a lot of information on the itertools functions, that are specifically created for efficient looping. This cuts the program run time to nearly a tenth of what I could get it to do with the other permuatation methods.
#http://stackoverflow.com/questions/11989502/producing-all-the-anagrams-from-a-string-python
#http://codereview.stackexchange.com/questions/52038/simple-anagram-or-permutation-generator-in-python

#import the itertools package for the permutaion function.
from itertools import permutations

#Method that permuatates the word list and then also compares the lists for the longest possible word. 
def permutate_and_compare(lst):
    perms = []
    j = 1
    for i in range (0, 9):
        perms += [''.join(p) for p in permutations(lst, j)]
        j += 1
    solved = compare_lists(words, perms)
    return solved

#Method to tie it altogether and solve the anagrams.
def solveAnagram(anagram):
    foundwords = []
    foundwords = anagram
    finalword = sorted(foundwords, key=len)
    print(finalword [-1])

def countdown():
    anagram = get_anagram()
    sorted_anagram = (''.join(sort_anagram(anagram)))
    perm_ana = permutate_and_compare(sorted_anagram)
    solveAnagram(perm_ana)

countdown()

#Using the time import I can check the efficiency of the and get the average time of the project over a set amount of loops through the project.
#https://docs.python.org/2/library/timeit.html

if __name__ == '__main__':
    import timeit
    numLoops = 50
    time = timeit.timeit("countdown()", setup="from __main__ import countdown", number=numLoops)
    print(time)
    print(numLoops, "Loops, Average of",  time/numLoops, "Seconds per loop" )

