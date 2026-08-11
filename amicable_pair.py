import math

def sum_proper_divisors(num):

    if num <= 1:
        return 0

    total_sum = 1

    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            total_sum += i
            if i != num // i:
                total_sum += num // i
    return total_sum

def is_amicable_pair(n1,n2):
    
    sum1 = sum_proper_divisors(n1)
    sum2 = sum_proper_divisors(n2)
            
    print(f'\nSum of proper divisors of {n1} is: {sum1}')
    print(f'Sum of proper divisors of {n2} is: {sum2}\n')

    if sum1 == n2 and sum2 == n1:
        print(f'{n1} and {n2} are AMICABLE numbers.')
    else:
        print(f'{n1} and {n2} are NOT amicable numbers.')


#Find amicable pairs up to a specific number (eg.10000)
def find_amicable_pairs(limit):

    div_sums = [0] * limit
    for i in range(1,limit):
        for j in range(2*i,limit,i):
            div_sums[j] += i

    pairs = []

    for num1 in range(1,limit):

        num2 = div_sums[num1]
        
        if num1 < num2 < limit and div_sums[num2] == num1:
            pairs.append((num1, num2))

    return pairs

def main():
    print(f'Amicable pairs up to 10000 are: \n',find_amicable_pairs(10000))

    print()
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))

        if num1 == num2:
            print(f'\nAmicable numbers must be distinct')
        else:
            is_amicable_pair(num1,num2)
        
    except ValueError:
        print('Invalid input. Please enter integers only.')   


# Run the program
if __name__ == "__main__":
    main()
