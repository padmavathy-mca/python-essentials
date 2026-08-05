Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Left Angle Triangle (LAT)
>>> #-------------------------
>>> for i in range(1,6):
...     for j in range(5,i,-1):
...         print(' ',end=' ')
...     for k in range(1,i+1):
...         print(k,end=' ')
...     print()
... 
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
>>> for i in range(5,0,-1):
...     for j in range(1,i):
...         print(' ',end=' ')
...     for k in range(i,6):
...         print(k,end=' ')
...     print()
... 
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(chr(k+64),end=' ')
    print()

        A 
      A B 
    A B C 
  A B C D 
A B C D E 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(chr(k+96),end=' ')
    print()

        a 
      a b 
    a b c 
  a b c d 
a b c d e 
for i in range(5,0,-1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(i,6):
        print(chr(k+64),end=' ')
    print()

        E 
      D E 
    C D E 
  B C D E 
A B C D E 
for i in range(5,0,-1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(i,6):
        print(chr(k+96),end=' ')
    print()

        e 
      d e 
    c d e 
  b c d e 
a b c d e 
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

name = 'padma'
for i in range(0,len(name)+1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()

          
        p 
      a a 
    d d d 
  m m m m 
a a a a a 
for i in range(0,len(name)+1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[k],end=' ')
    print()

          
        p 
      p a 
    p a d 
  p a d m 
p a d m a 
for i in range(1, len(name)+1):          
    for j in range(1, len(name)-i+1):     
        print(' ', end=' ')
    for k in range(len(name)-i, len(name)):       
        print(name[k], end=' ')
    print()

        a 
      m a 
    d m a 
  a d m a 
p a d m a 


#Inverse LAT
#-----------
for i in range(1, 6):             
    for j in range(5, i, -1):       
        print(' ', end=' ')
    for k in range(5, 5-i, -1):     
        print(k, end=' ')
    print()

        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1 

for i in range(1, 6):             
    for j in range(5, i, -1):       
        print(' ', end=' ')
    for k in range(i, 0, -1):       
        print(k, end=' ')
    print()

        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 
for i in range(1, 6):
    for j in range(5, i, -1):
        print(' ', end=' ')
    for k in range(5, 5-i, -1):
        print(chr(k+64), end=' ')
    print()

        E 
      E D 
    E D C 
  E D C B 
E D C B A 
for i in range(1, 6):
    for j in range(5, i, -1):
        print(' ', end=' ')
    for k in range(i, 0, -1):
        print(chr(k+64), end=' ')
    print()

        A 
      B A 
    C B A 
  D C B A 
E D C B A 
for i in range(1, 6):
    for j in range(5, i, -1):
        print(' ', end=' ')
    for k in range(5, 5-i, -1):
        print(chr(k+96), end=' ')
    print()

        e 
      e d 
    e d c 
  e d c b 
e d c b a 
for i in range(1, 6):
    for j in range(5, i, -1):
        print(' ', end=' ')
    for k in range(i, 0, -1):
        print(chr(k+96), end=' ')
    print()

        a 
      b a 
    c b a 
  d c b a 
e d c b a 

name = 'padma'
rev = name[::-1]
n = len(name)
for i in range(1, n+1):
    for j in range(n - i):
        print(' ',end=' ')
    for k in range(n - i, n):
        print(rev[k],end=' ')
    print()

        p 
      a p 
    d a p 
  m d a p 
a m d a p 


for i in range(1, n+1):             
    for j in range(n, i, -1):       
        print(' ',end=' ')
    for k in range(n-1, n-i-1, -1): 
        print(name[k],end=' ')
    print()

        a 
      a m 
    a m d 
  a m d a 
a m d a p 
