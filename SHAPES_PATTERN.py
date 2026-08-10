#Shapes co-ordinates        
circle = [(2,8), (2,7), (2,9), (3,5), (3,11), (4,4), (5,3), (7,2), (8,2), (11,3), (12,12), (11,13),
          (8,14), (7,14), (5,13), (4,12), (12,4), (13,5), (14,7), (14,8), (14,9), (13,11), (9,2), (9,14)]

semicircle = [(2,8), (2,7), (2,9), (3,5), (3,11), (4,4), (5,3), (7,2), (8,2), (8,14), (8,3), (8,4),
              (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,11), (8,12), (8,13), (7,14), (5,13), (4,12)]

oval = [(2,8), (2,7), (2,9), (3,5), (3,11), (4,4), (5,3), (7,2), (8,2), (11,3), (12,12), (11,13),
        (8,14), (7,14), (5,13), (4,12), (12,4), (13,5), (14,7), (14,8), (14,9), (13,11), (9,2), (9,14)]

heart = [(1,2), (1,3), (1,5), (1,6), (2,1), (2,4), (2,7), (3,1), (3,7), (4,2), (4,6), (5,3), (5,5), (6,4)]

square = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,1), (2,5), (3,1), (3,5), (4,1), (4,5), (5,1), (5,2),
          (5,3), (5,4), (5,5)]

rectangle = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (2,1), (2,8), (3,1), (3,8),
             (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8)]

triangle = [(1,4), (2,3), (2,5), (3,2), (3,6), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7)]

pentagon = [(1,4), (2,3), (2,5), (3,2), (3,6), (4,2), (4,6), (5,2), (5,6), (6,2), (6,3), (6,4), (6,5), (6,6)]

hexagon = [(1,3), (1,4), (1,5), (2,2), (2,6), (3,1), (3,7), (4,2), (4,6), (5,3), (5,4), (5,5)]

octagon = [(1,3), (1,4), (1,5), (2,2), (2,6), (3,1), (3,7), (4,1), (4,7), (5,2), (5,6), (6,3), (6,4), (6,5)]

heptagon = [(1,5), (2,4), (2,6), (3,3), (3,7), (4,2), (4,8), (5,2), (5,8), (6,2), (6,8), (7,3), (7,7), (8,4), (8,5), (8,6)]

parallelogram = [(1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (2,4), (2,9), (3,3), (3,8), (4,2), (4,7),
                 (5,1), (5,2), (5,3), (5,4), (5,5), (5,6)]

rhombus = [(1,4), (2,3), (2,5), (3,2), (3,6), (4,1), (4,7), (5,2), (5,6), (6,3), (6,5), (7,4)]

trapezium = [(1,5), (1,6), (1,7),(1,8), (2,4), (2,9), (3,3), (3,10), (4,2), (4,11),                                                          
             (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10),(5,11),(5,12)] 

def print_shape(shape, rows, cols=None):
    if cols is None:
        cols = rows 
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if (i, j) in shape:
                print('*', end=' ')
            else:
                print(' ', end=' ')

        print()

def main():
    print('*' * 100)
    print('2D Shapes'.center(100))
    print('*' * 100)
    print('Available Shapes')
    print('-' * 100)
    print('Circle | Semi circle | Oval     | Heart        | Rhombus ')
    print('Square | Rectangle   | Triangle | Pentagon     | Trapezium')
    print('Hexagon| Octagon     | Heptagon | Parallelogram')
    print('-' * 100)      

    sizes = {'circle':16, 'semicircle':(9,16), 'oval':16, 'heart':9, 'square':6,
        'rectangle':(6,12), 'triangle':(6,11), 'pentagon':7, 'hexagon':8,
        'octagon':8, 'heptagon':(8,11),'rhombus':7,'parallelogram':(5,10),'trapezium':(5,12)}
 
    # Normalize: convert every int into (int, int)
    for k, v in list(sizes.items()):
        if isinstance(v, int):
            sizes[k] = (v, v)
   
    user_input = input('Enter Shape: ')
    print()

    # Removes spaces at ends, converts to lowercase, AND removes spaces between words
    shape = user_input.strip().lower().replace(" ", "")
    
    if shape in sizes:
        shape_coords = globals()[shape]
        print_shape(shape_coords,*sizes[shape])
    else:
        print('Invalid Shape')

# Run the program
if __name__ == "__main__":
    main()  



'''
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

'''    



    
    
