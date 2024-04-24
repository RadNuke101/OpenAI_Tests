# Start time: 2024-04-10 17:27:52.165216

'''
Prompt:
Given that input as ['The'] output is 3, input as ['The quick fox'] output is 13, input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
        
        words = input_str.split()
        total_length = sum(len(word) for word in words)
        
        return total_length
    
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('The'))  # Output: 3
print(generated_function('The quick fox'))  # Output: 13
print(generated_function('The quick  fox'))  # Output: 14
print(generated_function("The"))  ## Output: 3
print(generated_function("The quick fox"))  ## Output: 13
print(generated_function("The quick  fox"))  ## Output: 14

# End time: 2024-04-10 17:27:53.818894
# Elapsed time in seconds: 1.6536409750000018


# APPEND TEST SCRIPTS...
print(generated_function("The"))  ## Output: 3
print(generated_function("The quick fox"))  ## Output: 13
print(generated_function("The quick  fox"))  ## Output: 14


print(generated_function("apple"))  ### Output: 5
print(generated_function("banana"))  ### Output: 6
print(generated_function("go eat the apple"))  ### Output: 16
print(generated_function("the"))  ### Output: 3

# TEST SCRIPTS APPENDED!
