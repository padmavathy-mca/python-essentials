Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Arbitrary Arguments
#-------------------
def add(*numbers):
    return sum(numbers)

print(add(1,2,3))
6
print(add(10,20,30))
60

def student_info(name,**details):
    print(f'Name: {name}')
    for key,value in details.items():
        print(f'{key}:{value}')

student_info('Padma',age=20,city='chennai')
Name: Padma
age:20
city:chennai
student_info('Padma',age=20,city='chennai',course='GenAI')
Name: Padma
age:20
city:chennai
course:GenAI

#Types of Arbitrary Arguments
#----------------------------
# *args - Arbitrary Positional Arguments
# **kwargs - Arbitrary Keyword Arguments

# Arbitrary Positional Arguments - Collects extra arguments into a tuple
# Arbitrary Keyword Arguments - Collects extra arguments into a dictionary

def greet(*winners):
    for name in winners:
        print(f'Congratulations, {name}!')

greet('Sanjay','Sara','Surya','Padma')
Congratulations, Sanjay!
Congratulations, Sara!
Congratulations, Surya!
Congratulations, Padma!

def build_car(**options):
    default = {'color':'white','doors':4}
    default.update(options)
    return default

print(build_car(color='red'))
{'color': 'red', 'doors': 4}
print(build_car(color='blue',doors=2,sunroof=True))
{'color': 'blue', 'doors': 2, 'sunroof': True}

def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

print(average(10,20,30))
20.0
print(average(5,15))
10.0

def aggregate(operation,*values):
    if not values:
        return None
    if operation == 'sum':
        return sum(values)
    elif operation == 'product':
        result = 1
        for v in values:
            result *= v
        return result
    elif operation == 'average':
        return sum(values)/len(values)
    elif operation == 'max':
        return max(values)
    elif operation == 'min':
        return min(values)
    else:
        return f'Unknown operation: {operation}'


print(aggregate('sum',1,2,3,4,5))
15
print(aggregate('product',2,3,4))
24
print(aggregate('average',15,25,35))
25.0
print(aggregate('max',7,2,6,3))
7
print(aggregate('min',7,3,6,4))
3

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 20
Added 20.0
Enter a number (or done): 30
Added 30.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'multiply', 'divide', 'power']: ADD
Result: 50

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 100
Added 100.0
Enter a number (or done): 25
Added 25.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'multiply', 'divide', 'power']: SUBTRACT
Result: 75

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 25
Added 25.0
Enter a number (or done): 4
Added 4.0
Enter a number (or done): 2
Added 2.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'multiply', 'divide', 'power']: MULTIPLY
Result: Unknown operation multiply

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 20
Added 20.0
Enter a number (or done): 30
Added 30.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'product', 'divide', 'power']: ADD
Result: 50

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 100
Added 100.0
Enter a number (or done): 25
Added 25.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'product', 'divide', 'power']: SUBTRACT
Result: 75

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 25
Added 25.0
Enter a number (or done): 4
Added 4.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'product', 'divide', 'power']: PRODUCT
Result: 100

======================= RESTART: D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 100
Added 100.0
Enter a number (or done): 4
Added 4.0
Enter a number (or done): DONE
Operation ['add', 'subtract', 'product', 'divide', 'power']: DIVIDE
Traceback (most recent call last):
  File "D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py", line 68, in <module>
    result = calc(*numbers,operation = op)
  File "D:/GEN-AI-10AM/PYTHON/FLEXIBLE_CALCULATOR.py", line 31, in calc
    result = number[0]
NameError: name 'number' is not defined. Did you mean: 'numbers'?

======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 100
Added 100.0
Enter a number (or done): 4
Added 4.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: divide
Result: 25.0

======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 12
Added 12.0
Enter a number (or done): 2
Added 2.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: power
Result: 144

======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 12
Added 12.0
Enter a number (or done): 3
Added 3.0
Enter a number (or done): 3
Added 3.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: power
Result: 1728

======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 12
Added 12.0
Enter a number (or done): 3
Added 3.0
Enter a number (or done): 2
Added 2.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: power
Result: Power needs exactly 2 numbers
>>> 
======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 25
Added 25.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: power
Result: Power needs exactly 2 numbers
>>> 
======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 25
Added 25.0
Enter a number (or done): 0
Added 0.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: divide
Result: Cannot divide by zero
>>> 
======================= RESTART: D:\GEN-AI-10AM\PYTHON\FLEXIBLE_CALCULATOR.py =======================
Enter a number (or done): 25
Added 25.0
Enter a number (or done): 3
Added 3.0
Enter a number (or done): 2
Added 2.0
Enter a number (or done): done
Operation ['add', 'subtract', 'product', 'divide', 'power']: divide
Result: 4.166666666666667
