#import ABC (Abstract Base Class)
#import abstractmethod decorator from abc module
from abc import ABC, abstractmethod

#ABSTRACT CLASS
class Person(ABC):

    #Constructor method - runs automatically when object is created
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def info(self):  #any child class must implement info()
        pass

#INHERITANCE
class Student(Person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll = roll
        self.__marks = []    #Private Identifier (ENCAPSULATION)

    #setter method - add to the private __marks list
    def add_marks(self,mark):  
        if 0 <= mark <= 100:   #validation
            self.__marks.append(mark)

    #getter method - provides read-only access to the private data
    def avg(self):
        return sum(self.__marks) / len(self.__marks) if self.__marks else 0

    def info(self):  #POLYMORPHISM
        return f'Student {self.name} (Roll no:{self.roll} Age:{self.age} Avg:{self.avg()}'

#INHERITANCE
class Teacher(Person):
    def __init__(self,name,age,subject): #constructor method 
        super().__init__(name,age)   #code reuse
        self.subject = subject      #new attribute specific to teacher

    def info(self):   #POLYMORPHISM
        return f'Teacher {self.name} (Subject:{self.subject}) Age:{self.age}'

def main():
    people = []  #empty list which stores both student and teacher objects

    while True:
        print('1.Add Student')
        print('2.Add Teacher')
        print('3.Show all details')
        print('4.Exit')

        choice = input('Enter choice: ')

        if choice == '1':
            name = input('Enter student name: ')
            age = int(input('Enter age: ')
            roll = int(input('Enter roll number: ')

            s = Student(name,age,roll)  #creates a student object 's'

            marks = input('Enter marks (comma-separated): ')
            for m in marks.split(','):       
                s.add_marks(int(m.strip())) #strip() - removes extra space from both ends 


            people.append(s)  #adds student object 's' to the people list
            print(f'Student {name} added!')

        elif choice == '2':
            name = input('Enter teacher name: ')
            age = int(input('Enter age: '))
            subject = input('Enter subject: ')

            people.append(Teacher(name,age,subject))  #create Teacher object and add it to the list
            print('f Teacher {name} added!')

        elif choice == '3':
            if not people:  #if people list is empty else list has items
                print('\n No records yet!')
            else:
                print('\n'+'='*50)
                for person in people:   #iterate through every object in the people list
                    print(person.info()) #calls the info() method on the current object (POLYMORPHISM)
                print('='*50)

        elif choice == '4':
            print('Goodbye!')
            break

        else:
            print('Invalid choice!')
    

    

    
    
    
