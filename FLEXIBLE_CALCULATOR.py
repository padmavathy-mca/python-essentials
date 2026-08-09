def get_valid_numbers():
    numbers = []
    while True:
        n = input('Enter a number (or done): ').strip()
        if n.lower() == 'done':
            break
        try:
            num = float(n)
            if num.is_integer():
                num = int(num)
            numbers.append(num)
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

def calc(*numbers,**options):

    #Get operation from options
    operation = options.get('operation')
    
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

# --- Main Program ---
def main():
    print("=" * 100)
    print("FLEXIBLE CALCULATOR".center(100))
    print("=" * 100)
    
    numbers = get_valid_numbers()
    if numbers:
        op = get_valid_operation()
        result = calc(*numbers,operation = op)
        print(f'Result: {result}')
        print("=" * 100)
    else:
        print('No numbers entered')
    
# Run the program
if __name__ == "__main__":
    main()    
    
