Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Comprehensions
#---------------------
#It is an expression that builds a new collection by:
#-Iterating over one or more existing iterables
#-Optionally filtering items with a condition
#-Optionally transforming each item
#-Collecting the results into a list,set,dictionary or generator
#All in a single readable expression

#List Comprehension
#------------------
#Find the squares of numbers (1-10) using for loop
squares = []
for n in range(1,11):
    squares.append(n**2)

print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Find the squares of numbers (1-10) using List comprehension
squares = [n**2 for n in range(1,11)]
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Print the squares without brackets
squares = [n**2 for n in range(1,11)]
print(*squares)
1 4 9 16 25 36 49 64 81 100

#Transforming String to uppercase
names = ['padma','surya','sanjay','sara']
upper_names = [names.upper() for name in names]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    upper_names = [names.upper() for name in names]
AttributeError: 'list' object has no attribute 'upper'
upper_names = [name.upper() for name in names]
print(upper_names)
['PADMA', 'SURYA', 'SANJAY', 'SARA']


#Transforming String to uppercase
names = ['padma','surya','sanjay','sara']
upper_names = [name.upper() for name in names]
print(upper_names)
['PADMA', 'SURYA', 'SANJAY', 'SARA']

#Dictionary Comprehension
#------------------------

3


#Transforming String to uppercase
names = ['padma','surya','sanjay','sara']
upper_names = [name.upper() for name in names]
print(upper_names)
['PADMA', 'SURYA', 'SANJAY', 'SARA']

#Dictionary Comprehension
#------------------------

#Number squares as key-value
square_dict = {x:x**2 for x in range(1,6)}
print(square_dict)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Get only vowels from the given string
text = 'python'
vowel_count = {char: text.count(char) for char in 'aeiou' if char in text}
print(vowel_count)
{'o': 1}

text = 'programming'
vowel_count = {char: text.count(char) for char in 'aeiou' if char in text}
print(vowel_count)
{'a': 1, 'i': 1, 'o': 1}

#Filtering a dictionary
prices = {'apple':25,'banana':12,'orange':30,'grapes':35}
affortable = {item:price for item,price in prices.items() if price < 30}
print(affortable)
{'apple': 25, 'banana': 12}

#Set Comprehension
#-----------------
#Get only the unique even numbers from a list with a condition
numbers = [1,2,2,3,3,3,4]
even_set = {n for n in numbers if n%2 == 0}
print(even_set)
{2, 4}

#Unique Squares from a list
numbers = [1,2,2,3,3,3,4]
unique_squares = {n**2 for n in numbers}
print(unique_squares)
{16, 1, 4, 9}

#Unique characters in a string
text = 'mississippi'
unique_chars = {c for c in text}
print(unique_chars)
{'s', 'i', 'm', 'p'}

#Generator Expression
#--------------------

#like List comprehension but Memory Efficient - doesn't store all values at once
#Uses parantheses

#Generator of squares
gen = (n**2 for x in range(1,11))
print(gen) #prints generator object
<generator object <genexpr> at 0x0000020B408C7E00>
print(list(gen))
[100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

#Generator of squares
gen = (n**2 for x in range(5))
print(gen) #prints generator object
<generator object <genexpr> at 0x0000020B409DBAC0>
print(list(gen))
[100, 100, 100, 100, 100]

>>> #Generator of squares
>>> gen = (n**2 for n in range(1,11))
>>> print(gen) #prints generator object
<generator object <genexpr> at 0x0000020B408C7E00>
>>> print(list(gen))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> #sum of squares
>>> total = sum(n**2 for n in range(1,11))
>>> print(total)
385
>>> 
>>> #Word length Analysis
>>> sentences = ["Python is great", "I love coding", "Comprehensions are useful"]
>>> word_lengths = [len(word) for sentence in sentences for word in sentence.split()]
>>> print(word_lengths)
[6, 2, 5, 1, 4, 6, 14, 3, 6]
>>> 
>>> #Find words starting with vowels
>>> words = ['apple','orange','python','sky','banana']
>>> vowels = [w for w in words if w[0].lower() in 'aeiou']
>>> print(vowels)
['apple', 'orange']
>>> 
>>> #Extract only numeric digits from a string
>>> text = 'Python 3.13'
>>> digits = [char for char in text if char.isdigit()]
>>> print(digits)
['3', '1', '3']
