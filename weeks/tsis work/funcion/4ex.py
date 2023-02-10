def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = [x for x in numbers if is_prime(x)]

print("Prime numbers in the list:", prime_numbers)
