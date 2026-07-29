Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Native Datatypes / Python Collections / Python Non-primitive datatypes
#-----------------------------------------------------------------------------
#Primitive Datatypes - store a single value and are completely immutable
# Int - holds positive / negative whole numbers
# Float - represents positive / negative decimal number
# Boolean - evaluates states of logic, exactly True or False
# String - contains sequence of characters enclosed in single/double quotation
# Complex - represent mathematical complex numbers (3 + 4j)

#NON PRIMITIVE DATATYPE - stores multiple values 
#----------------------
#List / Tuple / Set / Dictionary
#
#LIST
#----

#enclosed with [] - brackets
#list contains ordered collection of data items
#list values are indexed
#list values are mutable 
#list support duplicate values
#list contains heterogenous values

car = ['creta','wagonr','polo','creta','i20']
type(car)
<class 'list'>
car[0]
'creta'
car[1]
'wagonr'
car[2]
'polo'
car[3]
'creta'
car[4]
'i20'
car[0]==car[3]
True
car
['creta', 'wagonr', 'polo', 'creta', 'i20']
car[1]='venue'
car
['creta', 'venue', 'polo', 'creta', 'i20']
car[1:3]
['venue', 'polo']
car[2:]
['polo', 'creta', 'i20']
car[:2]
['creta', 'venue']

#List methods / List operations / List supporting functions
#----------------------------------------------------------

squares = [1,4,9,16,25]

squares.append(36)
squares
[1, 4, 9, 16, 25, 36]

squares.extend(['49','64'])

squares.index('9')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    squares.index('9')
ValueError: '9' is not in list
squares.index(9)
2
squares.insert(1,'two')
squares
[1, 'two', 4, 9, 16, 25, 36, '49', '64']
squares.insert(0,'one')
squares
['one', 1, 'two', 4, 9, 16, 25, 36, '49', '64']
squares.insert(4,'three')
squares
['one', 1, 'two', 4, 'three', 9, 16, 25, 36, '49', '64']
squares.insert(6,'four')
squares
['one', 1, 'two', 4, 'three', 9, 'four', 16, 25, 36, '49', '64']
squares.pop()
'64'
squares
['one', 1, 'two', 4, 'three', 9, 'four', 16, 25, 36, '49']
squares.pop()
'49'
squares
['one', 1, 'two', 4, 'three', 9, 'four', 16, 25, 36]
squares.remove('four')
squares
['one', 1, 'two', 4, 'three', 9, 16, 25, 36]
squares + [49,64,81,100]
['one', 1, 'two', 4, 'three', 9, 16, 25, 36, 49, 64, 81, 100]
squares.append(121)
squares
['one', 1, 'two', 4, 'three', 9, 16, 25, 36, 121]
squares.pop()
121
squares.pop(0)
'one'

dup_car = car   #shallow copy
dup_car
['creta', 'venue', 'polo', 'creta', 'i20']
>>> dup_car[2] = 'kushaq'
>>> dup_car
['creta', 'venue', 'kushaq', 'creta', 'i20']
>>> car
['creta', 'venue', 'kushaq', 'creta', 'i20']
>>> #The changes in the copied list also changed the original list.
>>> #This concept is called shallow copy

dup_sqr = squares.copy() #deep copy
dup_sqr
[1, 'two', 4, 'three', 9, 16, 25, 36]
dup_sqr.pop()
36
dup_sqr
[1, 'two', 4, 'three', 9, 16, 25]
squares
[1, 'two', 4, 'three', 9, 16, 25, 36]
#The changes in the copied list doesn't affect the original list.
#This concept is called deep copy.


>>> car.count('creta')
2
>>> car.sort()
>>> car
['creta', 'creta', 'i20', 'kushaq', 'venue']
>>> car.reverse()
>>> car
['venue', 'kushaq', 'i20', 'creta', 'creta']
>>> car.clear()
>>> car
[]
>>> 
>>> dup_car
[]
>>> squares.clear()
>>> squares
[]
>>> dup_sqr
[1, 'two', 4, 'three', 9, 16, 25]

dup_sqr.sort()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    dup_sqr.sort()
TypeError: '<' not supported between instances of 'str' and 'int'

dup_sqr.reverse()
dup_sqr
[25, 16, 9, 'three', 4, 'two', 1]
