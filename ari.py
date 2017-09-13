from sys import argv
import math

filename = argv[1]
no_Of_Words = 0
no_Of_Characters = 0
no_Of_Sentences = 0

file = open(filename)

read = file.read()
file.close()

grade = {1: "Kindergarten",
         2: "First Grade",
         3: "Second Grade",
         4: "Third Grade",
         5: "Fourth Grade",
         6: "Fifth Grade",
         7: "Sixth Grade",
         8: "Seventh Grade",
         9: "Eighth Grade",
         10: "Ninth Grade",
         11: "Tenth Grade",
         12: "Eleventh Grade",
         13: "Twelfth Grade",
         14: "College"
         }

content = read.replace('\n', ' ')
sentences = content.split('.')
words = content.split(' ')
no_Of_Characters = len(content)
no_Of_Sentences = len(sentences) - 1
no_Of_Words = len(words)

# print(f"no_Of_Characters : {no_Of_Characters}\nno_Of_Sentences : {no_Of_Sentences}\nno_Of_Words : {no_Of_Words}")

charByWord = no_Of_Characters / no_Of_Words
wordBySent = no_Of_Words / no_Of_Sentences
score = math.ceil((4.71 * charByWord) + (0.5 * wordBySent) - 21.43)
# score = 3
# print(f"score : {score}")

if score > 14:
    print(f"The Automated readability index for the given file, '{filename}' is {score}; its a suitable reading for Collage & adults.")
else:
    print(f"The Automated readability index for the given file, '{filename}' is {score}; its a suitable reading for {grade[score]}.")
