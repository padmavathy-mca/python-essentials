def find_factors(number):
    f_list = []
    for i in range(1,number+1):
        if number % i == 0:
            f_list.append(i)
    return f_list

n = int(input('Enter a number (small number): '))
print(f'Factors of the {n} are:',find_factors(n))


#find factors for large numbers
import math
def find_factors_for_ln(number):
    factors = set() # prevents duplicates
    for i in range(1, int(math.sqrt(number)) +1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(list(factors))

num = int(input('Enter a number (large number): '))
print(f'The factors of the {num} are: {find_factors_for_ln(num)}') 
                      
    
