def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)  # Fixed assignment
    num_digits = len(num_str)  # Fixed assignment
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  # Fixed exponentiation
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):  # Fixed missing colon
        if is_narc(num):  # Fixed function name and missing colon
            print(num)

print_narcis_numbers(1000, 5000)  # Fixed function name
