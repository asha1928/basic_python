def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """Print all prime numbers in the given range."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end}:")
print_primes_in_range(start, end)