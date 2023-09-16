#In the game SCRABBLE, each of the letters in the alphabet is assigned a value. 
#Each word would then have a value that is the sum of the values of its letters 
#(ignoring special spaces on the board). Using the values below, create a dictionary 
#to link letters to their values.

#Write a function word_value that takes a word as a parameter and returns the value 
#of the word by adding up the values of the letters using the dictionary. For example, 
#word_value("hello") should add 4+1+1+1+1 and return 8.

#Write another function called best_word that takes a list of words as a parameter 
#and uses the word_value function to determine which word is the highest scoring. 
#For example, best_word(["hello","world"]) should return "world" since "world" has a 
#value of 9.

#This program returns the scrabble score for a word and 
#returns the highest scoring word in a list of words. 
#Written by Srishti M. 
dict_letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, 
              "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, 
              "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, 
              "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, 
              "Y": 4, "Z": 10}

def word_value(word):
    score = 0
    for i in range(len(word)):
        score += dict_letters[word[i]]
    return score

print("The value of the word 'HELLO' is ", str(word_value("HELLO")))#Make sure word is spelt in all caps

def best_word(words):
    score = []
    for word in words:
        val = word_value(word)
        score.append(val)
    max_score = max(score)
    pos = score.index(max_score)
    return words[pos]
   
print("The best word among 'HELLO' and 'WORLD' based on each word's value is "+ str(best_word(['HELLO', 'WORLD'])))#Make sure words are spelt in all caps


            
