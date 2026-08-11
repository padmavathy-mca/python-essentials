def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def are_coprime(a,b):
    smaller = a if a < b else b

    for i in range(2, smaller + 1):
        if a % i == 0 and b % i == 0:
            return False

    return True

def main():
    print('-'*100)
    print('INTERACTIVE CHECKER'.center(100))
    print('-'*100)
    prime_nums = []
    for num in range(1,101):
        if is_prime(num):
            prime_nums.append(num)
        
    print('Prime numbers upto 100:\n',prime_nums)
    
    choice = input("\nType '1' to check a prime or '2' to check Co-Primes: ").strip()

    if choice == '1':
        num = int(input('Enter a number to check if it is prime: '))
        if is_prime(num):
            print(f'{num} is a PRIME number.')
        else:
            print(f'{num} is NOT a prime number. (it is a composite number)')

    elif choice == '2':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))

        if are_coprime(num1,num2):
            print(f'{num1} and {num2} are CO-PRIME. Their only common factor is 1')
        else:
            print(f'{num1},{num2} are NOT co-prime. They share a common factor')
    else:
        print('Invalid choice selected.')

# Run the program
if __name__ == "__main__":
    main() 




'''import math

def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    # Check divisibility up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def are_coprime(a, b):
    """Returns True if a and b are co-prime (GCD is 1), otherwise False."""
    return math.gcd(a, b) == 1
'''
