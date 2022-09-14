total = 0

for num in range(1, 1001):
    if num % 3 == 0 or num % 5 == 0:
        total += num

    # Prints 'fizzbuzz' for numbers that are divisible by 3 and 5.
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    # Prints 'fizz' for numbers that are divisible by 3.
    elif num % 3 == 0:
        print("fizz")
    # Prints 'buzz' for numbers that are divisible by 5.
    elif num % 5 == 0:
        print("buzz")
    # Just prints the remaining numbers.
    else:
        print(num)

print(total)
