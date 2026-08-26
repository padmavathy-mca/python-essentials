def write_patterns(filename):

    with open(filename, 'w') as f:
        
        f.write('Right angle triangle\n----------------------\n')
        for i in range(1, 6):
            line = str(i)* i
            f.write(line + '\n')    
        f.write('\n') 
            
        f.write('Left angle triangle\n----------------------\n')
        for i in range(1, 6):
            line = (" " * (5 - i)) + (str(i) * i)
            f.write(line + '\n')
        f.write('\n')
            
        f.write('Pyramid\n----------------------\n')
        for i in range(1, 6):
            line = (" " * (5 - i)) + (str(i) * (2 * i - 1))
            f.write(line + '\n')

def read_patterns(filename):
    with open(filename, 'r') as f:
        for i in f.readlines():
            print(i)

if __name__ == "__main__":

    filename = 'patterns.txt'
    write_patterns(filename)
    print('Patterns saved to file\n')
    read_patterns(filename)
    
