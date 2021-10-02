# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:49:28 2021

@author: rubenia

"""
tax = 12.5/100
price = 100.50
print(price*tax)

print('spam eggs')
print('doesn\'t')
print('"Yes" they said.')
print("\"Yes\" they said")      
print('Isn\'t," they said.')
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
print(s)
print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3*'un' + 'ium')

print('Py')
print('thon')
print('Py' + 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'Py'
print(prefix + 'thon' )

text = ('Put several strings in parenthesis ' 'to have them join together'
        'I did not know this trick!' ' ' 'Very' ' ' 'nice!')
print(text)

print('un'*3)
print('un'*3 + 'ium')

prefix = 'Py'

print(prefix + 'thon')

##### Indexing #####

##### Indexing is used to obtain individual characters

# Strings can be indexed (subscripted), with the first character having index 0
# There is no separate character type
# A character is simply a string of size 1

word = 'Python'

print(word[0]) # Character in position 0

print(word[5]) # Character in position 5

# Indices may also be negative numbers
# To use negative numbers start counting from the right

print(word[-1]) # Last character

print(word[-2]) # Second last character

print(word[-6])

# Since -0 is the same as 0, negative indices start from -1

##### Slicing #####

##### Slicing allows you to obtain a substring

print(word[0:2]) # Characters from position 0 (included) to 2 (excluded)

print(word[2:5]) # Characters from position 2 (included) to 5 (excluded)

##### Slice indices have useful defaults
##### An omitted first index defaults to zero
##### An omitted second index defaults to the size of the string being sliced
##### Note how the start is always included
##### Note how the end is always excluded
##### This makes sure that s[:i] + s[i:] is always equals to s
##### s[:i] + s[i:] = s

print(word[-6])

word = 'Python'
# Attempting to use an index that is too large will 
print(word[42])

# However, out of range slice indexes are handled gracefully when
# used for slicing
print(word[4:42])
print(word[42:])

##### Python strings cannot be changed. They are immutable. Therefore,
##### assigning to an indexed position in the string results in error.
word[0] = 'J'
word[2:] = 'py'

##### If you need a different string, you should create a new one
print('J' + word[1:])
print(word[:2] + 'py')
print('A' + 'B' + word[:5])
print(word[-3:] + 'XYZ')
print(word[-3:-1])

##### The built-in function len() returns the lenght of a string
s = 'abcdefghijklmn;opqrstuvwxyz'
print(len(s))
r = 'abcdefghijklmn;opqrstuvwxyz'
print(len(r))


