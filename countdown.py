#Import the time and random packages for timing how the program runs, and for randomising the anagram.
import random
import time
start_time = time.time()

#Readin from the file, populate a list with the contents of the file.
with open('sorted_words.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]

#Define an array to hold the anagram, additional arrays hold the consonants and vowels
anagram = []
vowels = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

#Three loops to satisfy the condition of having a set number of consontants and vowels, the third loop pulls from either a consonant or a vowel
for i in range (0,3):
    anagram.append(random.choice(vowels))
for i in range (0,4):
    anagram.append(random.choice(consonant))
for i in range (0,2):
    anagram.append(random.choice(vowels + consonant))

# Imports the shuffle function and shuffles the anagram
from random import shuffle
shuffle(anagram)

#Anagrams for testing, the objective is 9 lettered anagrams, however I keep a few anagrams with a small amount of letters to see how my methods fair.

#anagram = ['s','t','r','e','a','m','i','n','g']
#anagram = ['t', 'e', 's', 't']
#anagram = ['t', 'i', 'r', 'e', 'd']

#Prints the anagram
print (''.join(anagram))

#First atempt of permuatating every sequence of the anagram. Runs horribly slow and can use some optimisation.

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        anaPerm = []
        for i in range(len(lst)):
            pos = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                anaPerm.append([pos]+p)
        return anaPerm        

#Simple compare method that comapares two lists to see if the dictionary (sorted_words) contains the anagram. The compare method is fine with anagrams of small size, but with an anagram of 9 letters...i'd put the kettle on.

def comp(list1, list2):
    compAna = []
    for word in list1:
        comp = ''.join(sorted(word))
        if comp in list2:
            if (len(word) > 2):
                compAna.append(word)
            else:
                continue
    return compAna

#Method to tie it altogether and solve the anagrams.
def solveAna(anagram):
    perms = []
    perms += [''.join(p) for p in perm1(anagram)]
    solved = comp(words, perms)
    return solved
        
ana = solveAna(anagram)

print(ana)

print("--- %s seconds ---" % (time.time() - start_time))

