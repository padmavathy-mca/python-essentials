#Armstrong number or Narcissistic number

def isArmstrong(number):
    
    s = str(number)
    n = len(s)

    sum_digits = 0

    for d in s:
        sum_digits += int(d) ** n

    if sum_digits == number:
        return True
    else:
        return False

def find_armstrong():
    arm_list = []

    limit=10000
    for num in range(1,limit+1):
        if isArmstrong(num):
            arm_list.append(num)
    return arm_list
    
def main():
    print('Armstrong numbers till 10000 are: \n',find_armstrong())
    
    try:
        input_num = int(input('Enter a number to check: '))
    
        if isArmstrong(input_num):
            print(f'{input_num} is an Armstrong number.')
        else:
            print(f'{input_num} is NOT an Armstrong number.')
        
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main() 
