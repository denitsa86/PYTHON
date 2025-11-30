#Assign a multiline string to a variable by using three quotes
#Use the "+" operator to merge strings
#The "*" operator repeats the string
# 	Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)
# 	String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a)) #13
# 	Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt) #True

# 	Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5]) #llo
# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) # Hello
# Slice To the End
# By leaving out the end index, the range will go to the end:
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])  #llo, World!

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2]) #orl

# String Methods
# Check if a character is a digit: isdigit()
# Check if a character is upper/lower case: isupper() and islower()
# Convert to upper/lower case: upper() and lower()
# Remove white spaces in start/end or both: strip(), rstrip(), lstrip()
# You can use the replace() method to replace all occurrences of a specified phrase with another specified phrase
#The split() method returns a list where the text between the specified separator becomes the list items.
"""
Python has a set of built-in methods that you can use on strings.
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the 
"""