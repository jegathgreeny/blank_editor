import math

# Getting factors of a number.
def get_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // 2)
    return factors


# Find if a number is prime.
def is_prime(number):
    return len(get_factors(number)) == 2


all_factors = get_factors(600851475143)

large_prime_factor = 0
for factor in all_factors:
    # Checks if it's a prime factor and is greater than 0.
    if is_prime(factor) and factor > large_prime_factor:
        large_prime_factor = factor

print(large_prime_factor)
