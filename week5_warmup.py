# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
substring = magic.find ("c")
print(substring)
substring = magic[4:5]
print(substring)
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
substring = magic.find("r")
print(substring)
substring = magic[-2]
print(substring)
# c. Find the first occurrence of the letter 'c'.
magic = 'abracadabra'
substring = magic.find ("c")
print(substring)
substring = magic[4:5]
print(substring)

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
substring=alphabet.find ("hij")
print(substring)
substring=alphabet[7:10]
print(substring)
# b. Extract every second letter starting from 'a' to 'm'.
substring=alphabet.find("a")
print (substring)
substring=alphabet.find("m")
print (substring)
substring=alphabet[0:124:2]
print (substring)
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring=text.find ("John F. Kennedy")
print(substring)
substring=text.find ("dy")
print(substring)
substring=text[83:98]
print(substring)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
substring=info[36:-1]
print(substring)

# b. Extract every third word.
third=info[9:13]
print(third)
second=info[22:28]
print(second)
print(substring)

# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info[::-1])

# Problem Set 3: String Methods 
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
force="MAY THE FORCE BE WITH YOU"
print(force.lower())
print(force.upper())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
word_list=["Make", "haste", "slowly."]
joined_list=" ".join(word_list)
print(joined_list)
# b. Now, split the string at every occurrence of the letter 'a'.
occurrence=joined_list.split("a")
print(occurrence)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
life= "Life is what happens when you are busy making other plans."
subscript= life.replace("busy","distracted")
print(subscript)
# b. Replace "plans" with "mistakes".
subscript= life.replace("plans","mistakes")
print(subscript)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
iteration="iteration "*7
print(iteration)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
text2="Supercalifragilisticexpialidocious"
length = len(text2)
print(length)
# b. Count the number of times the letter 'i' appears in the same word/phrase
counting = text2.count ("i")
print(counting)
# Abel sanchez, Diego padilla