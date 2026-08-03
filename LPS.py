Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Looping Statements(LPS)
#-----------------------
#Same set of action repeated till n-1 times based on the given count

#for loop
#--------
#for loop follows CORM (Check Once Rus Manytimes) process
#for loop checks the condition only once and runs the loop (n-1) many times

for i in range(5):
    print(i)

0
1
2
3
4
for i in range(0,5,1):
    print(i)

0
1
2
3
4
for i in range(1,11,1):
    print(i,end=' ')

1 2 3 4 5 6 7 8 9 10 

#print even numbers (1-10)
for i in range(2,11,2):
    print(i,end=' ')

2 4 6 8 10 

#print odd numbers (1-10)
for i in range(1,11,2):
    print(i,end=' ')

1 3 5 7 9 

for i in range(1,11):
    if i%2 == 1:
        print(i,'-odd')
    else:
        print(i,'-even')

1 -odd
2 -even
3 -odd
4 -even
5 -odd
6 -even
7 -odd
8 -even
9 -odd
10 -even

#Iterative Statements
#--------------------
#Iterative means going through different elements of python collections (list/tuple/set/dictionary) using looping statements

country = ['India','Japan','Australia','Italy','Europe','USA','UAE']
for i in country:
    print(i)

India
Japan
Australia
Italy
Europe
USA
UAE

#print the country names which starts with 'I'
for i in country:
    if i.startswith('I'):
        print(i)

India
Italy

#print the country names which ends with 'a'
for i in country:
    if i.endswith('a'):
        print(i)

India
Australia

#print the country names whose character length is exactly 5
for i in country:
    if len(i) == 5:
        print(i)

India
Japan
Italy

#print the country names whose names starts with vowels
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in country:
    for j in vowels:
        if i.startswith(j):
            print(i)

India
Australia
Italy
Europe
USA
UAE

#print the country names whose names ends with vowels
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in country:
    for j in vowels:
        if i.endswith(j):
            print(i)

India
Australia
Europe
USA
UAE


#While loop
#----------
#Check the test condition every single time and runs the loop till the condition is true.
#It is mandate to give the incremental/decremental value in while loop
#Otherwise the loop will execute infinite times

a=10
while a>0:
    print(a)
    a -=1

10
9
8
7
6
5
4
3
2
1


count = 3
while count>0:
    print(count)
    count-=1

3
2
1

#Flow control Statements
#-----------------------

#break
#continue
#pass

#break - It terminates the execution of a loop when certain condition is met
for i in range(10):
    print(i,end=' ')

0 1 2 3 4 5 6 7 8 9 

for i in range(10):
    print(i,end=' ')
    if i==5:
        break

0 1 2 3 4 5 

for i in range(10):
    if i == 5:
        break
    print(i,end=' ')

0 1 2 3 4


#continue - It skips a particular value from the loop when certain condition is met and resumes the
#execution from next element.

for i in range(10):
    print(i,end=' ')
    if i==5:
        continue

0 1 2 3 4 5 6 7 8 9 

for i in range(10):
    if i==5:
        continue
    print(i,end=' ')

0 1 2 3 4 6 7 8 9 

#Display the numbers between 10 to 20 and skip numbers 15 and 18
for i in range(11,21):
    if i==15 or i==18:
        continue
    print(i,end=' ')

11 12 13 14 16 17 19 20 

name = ['padma','sara','aditi','sanjay','abhinav','surya']
#Display the names whose count is not exactly 5 using FCS
for i in name:
    if len(i)==5:
        continue
    print(i)

sara
sanjay
abhinav

 
#Display the names whose count is exactly 5 using FCS
for i in name:
...     if len(i)==5:
...         print(i)
... 
padma
aditi
surya
 
#Display the names whose count is not exactly 5 without using FCS
for i in name:
    if len(i)!=5:
        print(i)

sara
sanjay
abhinav
 
