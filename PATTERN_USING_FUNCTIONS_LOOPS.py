def star_rat():
    for i in range(1,6):
        for j in range(0,i):
            print('*',end=' ')
        print()
def star_lat():
    for i in range(1,6):
        for j in range(5,i,-1):
            print(' ',end=' ')
        for k in range(0,i):
            print('*',end=' ')
        print()
def star_pyramid():
    for i in range(1,6):
        for j in range(5,i,-1):
            print('',end=' ')
        for k in range(0,i):
            print('*',end=' ')
        print()

while True:
    print('-----------------')
    print('Available choices')
    print('-----------------')
    print('1.Star RAT')
    print('2.Star LAT')
    print('3.Star Pyramid')
    print('4.Exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        star_rat()
    elif choice == 2:
        star_lat()
    elif choice == 3:
        star_pyramid()
    elif choice == 4:
        exit()
    else:
        print('Enter valid choice')
        break
