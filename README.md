# Fixes and Improvements in Narcissistic Number Script

## Changes Made:
1. Fixed Function Definition Syntax Errors:
   - Added missing colons (`:`) at the end of function definitions.
   - Corrected parameter separation in `print_narcis_numbers(start, end)` by adding a comma.

2. Fixed Assignment Errors:
   - Changed `num_str == str(n)` to `num_str = str(n)`.
   - Changed `num_digits == len(num_str)` to `num_digits = len(num_str)`.

3. Fixed Exponentiation Operator:
   - Corrected `sum(int(digit) *** num_digits for digit in num_str)` to `sum(int(digit) ** num_digits for digit in num_str)`.

4. Fixed Function Name in Condition Check:
   - Changed `if is_narcissistic(num):` to `if is_narc(num):`, as `is_narcissistic` was not defined.

5. Fixed Loop and Conditional Syntax:
   - Added missing colons (`:`) in the `for` loop and `if` condition.

6. Fixed Incorrect Function Call at the End:
   - Changed `print_narc_numbers(1000, 5000)` to `print_narcis_numbers(1000, 5000)` to match the defined function.

The script now compiles and runs correctly, identifying and printing all narcissistic numbers in the given range.
