Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Collections / Non-primitive Datatypes
#--------------------------------------------
#List / Tuple / Set / Dictionary

#SET
#---
# Set is enclosed with {} - curly braces
# Set is an unordered collection of data items
# Set values are unindexed
# Set never supports duplicate values
# Set values are popped from beginning to end (FIFO)
# Set supports heterogenous values

basket = {'apple','orange','pear','banana'}
basket
{'orange', 'pear', 'apple', 'banana'}
type(basket)
<class 'set'>
basket.add('watermelon')
basket
{'pear', 'orange', 'watermelon', 'banana', 'apple'}
basket.add('orange')
basket
{'pear', 'orange', 'watermelon', 'banana', 'apple'}
basket.pop()
'pear'
basket
{'orange', 'watermelon', 'banana', 'apple'}
basket.remove('banana')
basket
{'orange', 'watermelon', 'apple'}
basket.update(['banana','pear'])
basket
{'pear', 'orange', 'watermelon', 'banana', 'apple'}
basket=frozenset(basket) #basket becomes immutable
basket
frozenset({'pear', 'orange', 'watermelon', 'banana', 'apple'})

#Set Operations
#--------------
squares = {1,4,9,16,25,36,49,64,81,100}
cubes = {1,8,27,64,125,216,343,512,729,1000}

squares
{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
cubes
{512, 1, 64, 8, 1000, 343, 216, 729, 27, 125}
squares.difference(cubes)
{100, 4, 36, 9, 16, 49, 81, 25}
cubes.difference(squares)
{512, 8, 1000, 343, 216, 729, 27, 125}
squares.intersection(cubes)
{64, 1}
cubes.intersection(squares)
{64, 1}
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
cubes
{512, 1, 64, 8, 1000, 343, 216, 729, 27, 125}
squares.discard(25)
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81}
squares.discard(45)
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81}

set1 = set()
#creates an empty set
set1
set()
type(set1)
<class 'set'>
set1.add(1)
set1.update([4,9,16,20])
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81}
set1
{1, 4, 9, 16, 20}
set1.difference_update(squares)
set1
{20}
set1.intersection_update(squares)
set1
set()
squares.intersection_update(set1)
squares
set()
set1.update([4,9,16,25])
set1
{16, 9, 4, 25}
set1.add(45)
set1
{4, 9, 45, 16, 25}
squares
set()
squares.update([1,4,9,16,25,36,49,64,81,100])
squares
{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
set1
{4, 9, 45, 16, 25}
set1.intersection_update(squares)
set1
{16, 9, 4, 25}
set1.issubset(squares)
True
squares.issuperset(set1)
True
set1.isdisjoint(squares)
False
set1.symmetric_difference(squares)
{64, 1, 36, 100, 49, 81}
set1.symmetric_difference_update(squares)
set1
{64, 1, 36, 100, 49, 81}

set2 = cubes.copy()
set2
{512, 1, 64, 8, 1000, 343, 216, 729, 27, 125}
set1.difference(set2)
{100, 49, 36, 81}
set1.intersection(set2)
{64, 1}
set2.isdisjoint(squares)
False
set2.clear()

set2.add(33)
set2.add(66)
set2
{33, 66}
set2.isdisjoint(set1)
True

