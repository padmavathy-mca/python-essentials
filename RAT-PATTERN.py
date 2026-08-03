Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#PATTERN PROGRAMS
#----------------

#Right Angle Triangle (RAT) - Using nested for loop
#--------------------------------------------------
for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print()

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5


# i - represents outer for loop / Row Printing / which number to print
# j - represents inner for loop / Column Printing/ how many times to print


for i in range(1,6):
    for j in range(0,i):
        print(j,end=' ')
    print()

0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

for i in range(1,6):
    for j in range(0,i):
        print('*',end=' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * * 

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

A 
B B 
C C C 
D D D D 
E E E E E 
 
for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

A 
A B 
A B C 
A B C D 
A B C D E 

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

a 
b b 
c c c 
d d d d 
e e e e e 

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

a 
a b 
a b c 
a b c d 
a b c d e 

#Inverse RAT pattern printing
#----------------------------

#Row printing (Numbers) 
for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

#Column printing (Numbers)
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()

5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5

#Star printing
for i in range(5,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print()

* * * * * 
* * * * 
* * * 
* * 
* 

#Row printing (Uppercase)
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

E E E E E 
D D D D 
C C C 
B B 
A 

#Column printing (Uppercase)
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(chr(j+64),end=' ')
    print()

E D C B A 
E D C B 
E D C 
E D 
E 

 
#Row printing (Lowercase)
>>> for i in range(5,0,-1):
...     for j in range(0,i):
...         print(chr(i+96),end=' ')
...     print()
... 
e e e e e 
d d d d 
c c c 
b b 
a

#Column printing (Lowercase)
>>> for i in range(1,6):
...     for j in range(5,i-1,-1):
...         print(chr(j+96),end=' ')
...     print()
... 
e d c b a 
e d c b 
e d c 
e d 
e 
