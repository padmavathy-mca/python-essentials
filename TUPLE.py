Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#NON PRIMITIVE DATATYPE
#----------------------

#TUPLE
#-----
#  Tuple is enclosed with () - paranthesis
#  Tuple values are ordered collection of data items
#  Tuple values are indexed
#  Tuple supports duplicate values
#  Tuple values are immutable
#  Tuple also contains heterogenous values

t = ('padma','sara','aditi','surya','padma','aditi')
>>> type(t)
<class 'tuple'>
>>> 
>>> #Tuple operations - count() and index()
>>> t
('padma', 'sara', 'aditi', 'surya', 'padma', 'aditi')
>>> t.count('padma')
2
>>> t.index('sara')
1
>>> 
>>> #Ways to update values in a tuple
>>> t = list(t) #convert tuple to list
>>> t.append('abhinav')
>>> t
['padma', 'sara', 'aditi', 'surya', 'padma', 'aditi', 'abhinav']
>>> type(t)
<class 'list'>
>>> t = tuple(t) #convert list to tuple
>>> type(t)
<class 'tuple'>
>>> 
>>> #Tuple Concatenation
>>> t1 = (10,20,10,20)
>>> t = t + t1
>>> t
('padma', 'sara', 'aditi', 'surya', 'padma', 'aditi', 'abhinav', 10, 20, 10, 20)
