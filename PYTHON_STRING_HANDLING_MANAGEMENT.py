Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String Handling Management
#--------------------------
#String Indexing - way to access individual characters in a string using its index value.
#Index value of a string starts from 0.
text = "python programming"
#Positive Indexing
text[0]
'p'
text[1]
'y'
text[2]
't'
text[3]
'h'
text[4]
'o'
text[5]
'n'
text[6]
' '
#Spaces are also characters so it will take an index position.
text[7]
'p'
text[8]
'r'
text[9]
'o'
text[10]
'g'
text[11]
'r'
text[12]
'a'
text[13]
'm'
text[14]
'm'
text[15]
'i'
text[16]
'n'
text[17]
'g'
#text[18] - IndexError: string index out of range
text[18]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    text[18]
IndexError: string index out of range

#Negative Indexing
text[-1]
'g'
text[-2]
'n'
text[-3]
'i'
text[-4]
'm'
text[-5]
'm'
text[-6]
'a'
text[-7]
'r'
text[-8]
'g'
text[-9]
'o'
text[-10]
'r'
text[-11]
'p'
text[-12]
' '
text[-13]
'n'
text[-14]
'o'
text[-15]
'h'
text[-16]
't'
text[-17]
'y'
text[-18]
'p'

#String Slicing - extract a particular portion of a string using (start:stop)
text
'python programming'
text[0:6]
'python'
text[7:18]
'programming'

#String ranging - almost similar to slicing but start/stop is optional here.
text[:6]
'python'
text[7:]
'programming'
text[-11:]
'programming'
text[:-12]
'python'

#String reverse - arrange the given string characters in reverse order using (start:stop:step)
text[::-1]
'gnimmargorp nohtyp'
text[::-2]
'gimropnhy'
text[::-3]
'gmrrnt'
text
'python programming'

#String concatenation - using '+' operator
text_1 = 'python'
text_2 = 'programming'
text_1 + text_2
'pythonprogramming'
'10'+'10'
'1010'
#Type Error: 'python' + 10 (can only conatenate string)
'python' + 10
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    'python' + 10
TypeError: can only concatenate str (not "int") to str

'100' + '100'
'100100'

#String repetition - using '*' operator
text_1
'python'
text_1 * 5
'pythonpythonpythonpythonpython'
'10' * 5
'1010101010'
'100' * 3
'100100100'
'Hello World' * 6
'Hello WorldHello WorldHello WorldHello WorldHello WorldHello World'

#String formatting
name = 'aditi'
age = 23
#Manual formatting - using str.format() method
print("Hello, {}. You are {} years old.".format(name,age))
Hello, aditi. You are 23 years old.
print("Hello, {0}. You are {1} years old.".format(name,age))
Hello, aditi. You are 23 years old.
print('Hello, {1}. You are {0} years old.'.format(age,name))
Hello, aditi. You are 23 years old.

#Automatted formatting - using % formatting (%s for strings , %d for integers)
print('Hello, %s. You are %d years old.' % (name,age))
Hello, aditi. You are 23 years old.

#General formatting
print('Hello, ',name,'You are ',age,'years old.')
Hello,  aditi You are  23 years old.

#Formatted String / f-strings which was introduced in Python 3.6
print(f'Hello, {name}.You are {age} years old.')
Hello, aditi.You are 23 years old.

#String supporting functions / dotted functions
name
'aditi'
name.capitalize()
'Aditi'
name.lower()
'aditi'
name.upper()
'ADITI'
name.casefold()
'aditi'
name.find('d')
1
name.find('s')
-1
name.index('i')
2
name.rindex('i')
4
name.rfind('i')
4
name.find('i')
2
name.index('s') # Error - substring not found
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    name.index('s') # Error - substring not found
ValueError: substring not found
name.center(50)
'                      aditi                       '
name.ljust(50)
'aditi                                             '
name.rjust(50)
'                                             aditi'
'250'.zfill(10)
'0000000250'
'250'.center(10,'*')
'***250****'
name.ljust(10,'*')
'aditi*****'
name.rjust(10,'*')
'*****aditi'
'250'.ljust(15,'*')
'250************'
'250'.rjust(15,'*')
'************250'
'     Python      '.strip()
'Python'
'     Python      '.lstrip()
'Python      '
'     Python      '.rstrip()
'     Python'
'####Python Programming####'.strip('#')
'Python Programming'
'www.python.org'.strip('w.org')
'python'
name
'aditi'
name.count('i')
2
name.endswith('k')
False
name.endswith('i')
True
name.startswith('a')
True
name.startswith('j')
False
'-'.join(['python','programming','tutorial'])
'python-programming-tutorial'
'/'.join(['01','mar','2003'])
'01/mar/2003'
'www.python.org'.partition('.')
('www', '.', 'python.org')
'www.python.org'.rpartition('.')
('www.python', '.', 'org')
'pop-oops'.partition('-')
('pop', '-', 'oops')
name
'aditi'
name.strip('i')
'adit'
'malayalam'.strip('m')
'alayala'
'malayalam'.removeprefix('m')
'alayalam'
'malayalam'.removeprefix('mal')
'ayalam'
'malayalam'.removesuffix('m')
'malayala'
'malayalam'.removesuffix('mal')
'malayalam'
'malayalam'.removesuffix('s')
'malayalam'
'python programming'.replace('p','P')
'Python Programming'
'python programming'.title()
'Python Programming'
text
'python programming'
text.isalnum()
False
text.isalpha()
False
text.isascii()
True
text.isdecimal()
False
'python123'.isalnum()
True
'python'.isalnum()
True
'python123'.isalpha()
False
'python'.isalpha()
True
>>> 'python123'.isdecimal()
False
>>> '123'.isdecimal()
True
>>> 'python123'.isnumeric()
False
>>> 'python_123'.isnumeric()
False
>>> 'VI'.isnumeric()
False
>>> '123'.isnumeric()
True
>>> '123'.isprintable()
True
>>> 'python'.isprintable()
True
>>> 'python'.isidentifier()
True
>>> 'python123'.isidentifier()
True
>>> 'python'.islower()
True
>>> 'python programming'.isspace()
False
>>> ' '.isspace()
True
