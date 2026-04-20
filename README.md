# Group-Anagram
Solved group anagram using string manipulation and hashing techniques
##Algorithm
-initialise an empty dict to store
-loop through each word in input list
sort the char in the word and join them back to a  string
-check if signature present in the dict
-if not present create a new list 
-add the current word to the list corresponding to its signature
-return all the grouped list
#Complexity;
TIME=O(n klogk)
SPACE=O(nk)
