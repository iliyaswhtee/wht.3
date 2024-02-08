def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Example:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print(prime_numbers)