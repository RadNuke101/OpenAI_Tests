# Start time: 2024-04-10 17:28:29.917810

'''
Prompt:
Given that input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_str = input_str.strip()
        if len(input_str) != 12:
            raise ValueError("Input string length should be 12 characters")

        area_code = input_str[:3]
        first_part = input_str[4:7]
        second_part = input_str[8:]

        return f"{area_code}-{first_part}-{second_part}"

    except ValueError as ve:
        return f"Error: {ve}"

# Test cases
print(generated_function('801 456 8756'))  # Output: 801-456-8756
print(generated_function('978 456 8756'))  # Output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 17:28:31.853303
# Elapsed time in seconds: 1.9354507300000137


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!

