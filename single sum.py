def digital_root(n):
    while n >= 10:  # Continue until a single-digit number is obtained
        n = sum(int(digit) for digit in str(n))  # Convert number to string, iterate through digits, sum them
    return n


num = int(input("Enter a number: "))
result = digital_root(num)
print(f"The single-digit sum (digital root) of {num} is: {result}")