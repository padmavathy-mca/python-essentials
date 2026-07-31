Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Decision Making Statements(DMS) / Conditional Statements
... #--------------------------------------------------------
... #if
... 
... name = 'padma'
>>> if name == 'padma':
...     print('Name is matched')
... 
Name is matched
>>> 
>>> #if...else
... age = 18
>>> if age >= 18:
...     print('Eligible for Voting')
... else:
...     print('Not Eligible for Voting')
... 
Eligible for Voting
>>> 
>>> age = 13
>>> if age >= 18:
...     print('Eligible for Voting')
... else:
...     print('Not Eligible for Voting')
... 
Not Eligible for Voting

#if...elif...else
number = 20
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is zero')

Number is positive

number = 0
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is zero')

Number is zero

number = -1
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is zero')

Number is negative

#Student Grading System
score = 81
if score >= 91 and score <=100:
    print(score,'Grade S')
elif score >= 81 and score <= 90:
    print(score,'Grade A')
elif score >= 71 and score <= 80:
    print(score,'Grade B')
elif score >=61 and score <= 70:
    print(score,'Grade C')
elif score >=51 and score <= 60:
    print(score,'Grade D')
elif score == 50:
    print(score,'Grade E')
elif score < 50:
    print(score,'U - fail')
else:
    print('Enter valid score')
    
SyntaxError: multiple statements found while compiling a single statement

#Student Grading System
score = 81
if score >= 91 and score <=100:
    print(score,'Grade S')
elif score >= 81 and score <= 90:
    print(score,'Grade A')
elif score >= 71 and score <= 80:
    print(score,'Grade B')
elif score >=61 and score <= 70:
    print(score,'Grade C')
elif score >=51 and score <= 60:
    print(score,'Grade D')
elif score == 50:
    print(score,'Grade E')
elif score < 50:
    print(score,'U - fail')
else:
    print('Enter valid score')

81 Grade A

score = 54
if score >= 91 and score <=100:
    print(score,'Grade S')
elif score >= 81 and score <= 90:
    print(score,'Grade A')
elif score >= 71 and score <= 80:
    print(score,'Grade B')
elif score >=61 and score <= 70:
    print(score,'Grade C')
elif score >=51 and score <= 60:
    print(score,'Grade D')
elif score == 50:
    print(score,'Grade E')
elif score < 50:
    print(score,'U - fail')
else:
    print('Enter valid score')

54 Grade D

score = 101
if score >= 91 and score <=100:
    print(score,'Grade S')
elif score >= 81 and score <= 90:
    print(score,'Grade A')
elif score >= 71 and score <= 80:
    print(score,'Grade B')
elif score >=61 and score <= 70:
    print(score,'Grade C')
elif score >=51 and score <= 60:
    print(score,'Grade D')
elif score == 50:
    print(score,'Grade E')
elif score < 50:
    print(score,'U - fail')
else:
    print('Enter valid score')

Enter valid score

#Nested if 

#Driving Eligibility and License Check
age = 20
has_license = True
SyntaxError: multiple statements found while compiling a single statement

#Nested if

#Driving Eligibility and License Check
age = 20
has_license = True
if age >= 18:
    if has_license:
        print('You are allowed to drive')
    else:
        print('You are old enough, but you need a driving license')
else:
    print('You are too young to drive')

You are allowed to drive


#User Login Validation
input_username = 'admin'
input_password = 'admin@123'
db_username = 'admin'
db_password = 'admin@123'
account_active = True
if input_username == db_username:
    if input_password == db_password:
        if account_active:
            print('Login successful. Welcome!')
        else:
            print('Login Failed: Account is deactivated')
    else:
        print('Login Failed: Incorrect password')
else:
    print('Login Failed: Username not found')

Login successful. Welcome!


input_username = 'admin'
input_password = 'admin123'
if input_username == db_username:
    if input_password == db_password:
        if account_active:
            print('Login successful. Welcome!')
        else:
            print('Login Failed: Account is deactivated')
    else:
        print('Login Failed: Incorrect password')
else:
    print('Login Failed: Username not found')

Login Failed: Incorrect password


#Match statements

day = 'Saturday'
match day.lower():
    case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday':
        print('Weekday. Back to work!')
    case 'saturday' | 'sunday':
        print('Weekend. Time to relax')
    case _:
        print('Invalid day entered')

Weekend. Time to relax

day = 'MONDAY'
match day.lower():
    case 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday':
        print('Weekday. Back to work!')
    case 'saturday' | 'sunday':
        print('Weekend. Time to relax')
    case _:
        print('Invalid day entered')

Weekday. Back to work!



