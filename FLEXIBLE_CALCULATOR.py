def calc(*numbers,**options):

    #validation for *args (numbers)
    if not numbers:
        return 'Error: No numbers provided!'
    
    #extract options from **kwargs with defaults
    operation = options.get('operation','add')

    #validate operation
    valid_ops = ['add','subtract','product','divide','power']
    if operation not in valid_ops:
        return f'Unknown operation {operation}'

    #Perform Calculation
    if operation == 'add':
        return sum(numbers)
    elif operation == 'subtract':
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result
    elif operation == 'product':
        result = 1
        for n in numbers:
            result *= n
        return result
    elif operation == 'divide':
        if len(numbers) < 2:
            return 'Division needs atleast 2 numbers'
        result = numbers[0]
        for n in numbers[1:]:
            if n == 0:
                return 'Cannot divide by zero'
            result /= n
        return result
    elif operation == 'power':
        if len(numbers) != 2:
            return 'Power needs exactly 2 numbers'
        return numbers[0] ** numbers[1]

def get_valid_numbers():
    numbers = []
    while True:
        n = input('Enter a number (or done): ').strip()
        if n.lower() == 'done':
            break
        try:
            num = float(n)
            numbers.append(int(num) if num.is_integer() else num)
            print(f'Added {num}')
        except ValueError:
            print('Invalid Input')
    return numbers

def get_valid_operation():
    valid_ops = ['add','subtract','product','divide','power']
    while True:
        op = input(f'Operation {valid_ops}: ').strip().lower()
        if op in valid_ops:
            return op
        print('Invalid Operation')


numbers = get_valid_numbers()
if numbers:
    op = get_valid_operation()
    result = calc(*numbers,operation = op)
    print(f'Result: {result}')
else:
    print('No numbers entered')
    
    
    
