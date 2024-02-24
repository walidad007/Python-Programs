
''' 
To create acronyms using python, we need to write a python program that
generates a short form of a word from a given sentence. we can do this by spliting
and indexing to get the first word and then combine it.

'''

# this line prompts user to input a phrase 
user_input = str(input("Enter a Phrase: "))

# split your typed input string into a list of words,it splits on whit spaces.
text = user_input.split()

# This initializes a string a with a single space. 
# It seems that you intend to collect the first letters of each 
# word in this string.
a = " "

# This is a loop that iterates over each word in the text list.
for i in text:
    
    '''For each word i, it takes the first character i[0], 
    converts it to uppercase using .upper(), 
    converts it to string using str(), 
    and then appends it to the string a. 
    This line effectively collects the first letter of 
    each word and appends it to the string a.'''
    a = a + str(i[0].upper())

print(a)
