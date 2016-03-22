#Readin from the file
with open('words.txt', 'r') as fileopen:
    words = [line.strip() for line in fileopen]
    
    
    
#Experimented with different types of sorting for the dictionary.

#Using the list.sort() method sorts a list into ascending order. The list.sort() method does not create a new list, and therefore can be faster if the list is already populated.

#words.sort()
#print(words)

#The sorted function takes in a list, then creates a new list with the list elements sorted. Therefore the original list is not altered.

#sort_words = sorted(words, key=len)
#print (sort_words)

#Additionally the sorted function can take an optional "key" parameter. The key value takes in a value and returns another value, which is then used for comparisons within the sort.

#sort_words = sorted(words, key = len)
#print(sort_words)

#Using the sorted function additional functionality can be added to the sorting function, such as the reverse option.

sort_words = sorted(words, key=len, reverse=True)
#print(sort_words)

#Using a for each i iterate through each word checking to see if the word exceeds a word lenght of 10. I then write the word to a file.

fopen = open("sorted_words.txt", "w")

for word in sort_words:
    if len(word) < 10:
        #print(word)
        fopen.write("%s\n" % word)
        
#By sorting the dictionary into an alphabitised word list I should be able to increase the optimisation of searching the dictionary for an anagram. 
        