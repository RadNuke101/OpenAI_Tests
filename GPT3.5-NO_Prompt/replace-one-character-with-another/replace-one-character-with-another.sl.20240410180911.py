# Start time: 2024-04-10 18:15:27.076146

'''
Prompt:
Given that input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string by space
        parts = input_str.split()
        
        # Check if there are exactly 3 parts
        if len(parts) != 3:
            raise ValueError("Input format is incorrect")
        
        # Join the parts with hyphens and return the result
        return "-".join(parts)
    
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('801 456 8756'))
print(generated_function('978 456 8756'))
print(generated_function('1234567890'))
print(generated_function('abc def ghi'))
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 18:15:29.228252
# Elapsed time in seconds: 2.151407158999973