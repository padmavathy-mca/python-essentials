def heart():
    heart_points = [(1,2),(1,3),(1,5),(1,6),(2,1),(2,4),(2,7),(3,1),(3,7),(4,2),(4,6),
                         (5,3),(5,5),(6,4)]
    for i in range(1,9):
        for j in range(1,9):
            if (i,j) in heart_points:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
def square():
    square_points = [(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,5),(3,1),(3,5),(4,1),(4,5),
                          (5,1),(5,2),(5,3),(5,4),(5,5)]
    for i in range(1,6):
        for j in range(1,6):
            if (i,j) in square_points:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
def rectangle():
        rectangle_points = [
        (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
        (1,7), (1,8), (1,9), (1,10),
        (2,1), (2,10),
        (3,1), (3,10),
        (4,1), (4,10),
        (5,1), (5,10),
        (6,1), (6,2), (6,3), (6,4), (6,5), (6,6),
        (6,7), (6,8), (6,9), (6,10),
    ]
        for i in range(1,8):
           for j in range(1,12):
               if (i,j) in rectangle_points:
                   print('*', end=' ')
               else:
                   print(' ', end=' ')
           print()
           
def triangle():
    triangle_points = [(1,6),
        (2,5),(2,7),
        (3,4),(3,5),(3,6),(3,7),(3,8),
        (4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),
        (5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),]
    for i in range(6):
        for j in range(11):
            if (i,j) in triangle_points:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    
print('Available Choices of 2D Shapes')
print('---------------------------')
print('1.Heart Shape Pattern')
print('2.Square Shape Pattern')
print('3.Rectangle Shape Pattern')
print('4.Triangle Shape Pattern')
print('5.Exit')

while True:
    choice = int(input('Enter your choice: '))
    print()
    if choice == 1:
        heart()
    elif choice == 2:
        square()
    elif choice == 3:
        rectangle()
    elif choice == 4:
        triangle()
    elif choice == 5:
        exit()
    else:
        print('Invalid Choice')
        break


    
    
