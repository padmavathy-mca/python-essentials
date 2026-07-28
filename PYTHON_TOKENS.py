Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#PYTHON TOKENS
'''LANGUAGE COMONENTS
IDENTIFIERS
LITERALS
OPERATORS
KEYWORDS
COMMENTS
QUOTATIONS '''
'LANGUAGE COMONENTS\nIDENTIFIERS\nLITERALS\nOPERATORS\nKEYWORDS\nCOMMENTS\nQUOTATIONS '
#Identifiers - Variables / Value Containers
name = 'padma'
age = 36
city = 'chennai'
#Identifiers Types
'''
Private Identifiers
Strong Private Identifiers
Magical method identifiers
'''
'\nPrivate Identifiers\nStrong Private Identifiers\nMagical method identifiers\n'
_name = 'padma' #private identifier
__name = 'divya' #strong private identifier
a = 20
b = 30
a.__add__(b)
50
a.__add__(b) #magical method identifier
50
#Literals - checking the exact datatype of a value stored in the identifier
type(name)
<class 'str'>
type(age)
<class 'int'>
type(city)
<class 'str'>
type(3.14)
<class 'float'>
#Operators
'''
Arithmetic operators (+ - * / % //)
Logical operators(and or not)
Relational operator(> >= < <= == !=)
Assignment operator(= += -= *= /= %= //=)
Membership operator(in not in)
Identity operators(is is not)
'''
'\nArithmetic operators (+ - * / % //)\nLogical operators(and or not)\nRelational operator(> >= < <= == !=)\nAssignment operator(= += -= *= /= %= //=)\nMembership operator(in not in)\nIdentity operators(is is not)\n'
#Arithmetic operators (+ - * / % //)
a + b
50
a - b
-10
a * b
600
a / b
0.6666666666666666
a % b
20
a // b
0
a
20
b
30
divmod(48,5)
(9, 3)
#Logical operators(and or not)
a
20
b
30
a == 20 and b == 30
True
a ==10 and b == 30
False
a == 20 or b == 40
True
a == 2 or b == 4
False
#Relational operator(> >= < <= == !=)
a
20
b
30
a > b
False
a >= b
False
a < b
True
a <= b
True
a == b
False
a != b
True
#Assignment operator(= += -= *= /= %= //=)
a
20
a = 30
#here value of 'a' is updated
a
30
a += 10 # a = a + 10
a
40
a -= 5 # a = a - 5
a
35
a *= 2 # a = a * 2
a
70
a /= 5 # a = a / 5
a
14.0
a %= 3 # a = a % 3
a
2.0
a //= 2 # a = a // 2
a
1.0
a = int(a)
a
1
#Membership operator(in not in)
'a' in 'padma'
True
'b' in 'padma'
False
'a' not in 'padma'
False
'b' not in 'padma'
True
#Identity operators(is is not)
a
1
b
30
a == 1
True
a is 1
True
b is not 1
True
a is not 1
False
b is 30
True
b is not 30
False
a is not 30
True
#Identity operators are used in payment gateways / wifi password validation
#Membership operators are used in contact book(search)/ dialpad launcher/ google search/ gmaps search

#KEYWORDS - reserved word with a specific meaning
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

'''
Looping statements(LPS)      ---> for / while
Decision making stmts(DMS)   ---> if / else / elif
Flow control statements(FCS) ---> break / continue / pass
User defined functions       ---> def / return / yield
OOPS                         ---> class / del /
Exception handling           ---> try / except / finally
Boolean logic values         ---> True / False
Modules programming          ---> import / from / as
Logical operator             ---> and / or / not
File handling                ---> with
'''
'\nLooping statements(LPS)      ---> for / while\nDecision making stmts(DMS)   ---> if / else / elif\nFlow control statements(FCS) ---> break / continue / pass\nUser defined functions       ---> def / return / yield\nOOPS                         ---> class / del /\nException handling           ---> try / except / finally\nBoolean logic values         ---> True / False\nModules programming          ---> import / from / as\nLogical operator             ---> and / or / not\nFile handling                ---> with\n'
#COMMENTS AND QUOTATIONS
#Single line comments
''' Multi line
comments'''
' Multi line\ncomments'
>>> 
=========================== RESTART: D:/GEN-AI-10AM/multi_line_comments.py ==========================
padma
surya
sanjay
sara
abhinav
aditi
>>> 
=========================== RESTART: D:/GEN-AI-10AM/multi_line_comments.py ==========================
padma
surya
sanjay
sara
>>> 
=========================== RESTART: D:/GEN-AI-10AM/multi_line_comments.py ==========================
sanjay
sara
abhinav
aditi
>>> 
=========================== RESTART: D:/GEN-AI-10AM/multi_line_comments.py ==========================
padma
surya
abhinav
aditi
