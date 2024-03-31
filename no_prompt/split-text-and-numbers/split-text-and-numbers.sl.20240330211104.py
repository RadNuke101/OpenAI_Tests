# Start time: 2024-03-30 21:17:23.192103

# Content: Given that given input as ['apples30', '7'] output is apples, given input as ['peaches24', '8'] output is peaches, given input as ['peaches0', '8'] output is peaches, given input as ['pears', '6'] output is pears, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_fruit_name(input_str):
    try:
        # Input: 'apples30', '7'
        # Output: 'apples'
        
        # Input: 'peaches24', '8'
        # Output: 'peaches'
        
        # Input: 'peaches0', '8'
        # Output: 'peaches'
        
        # Input: 'pears', '6'
        # Output: 'pears'
        
        fruit_name = ''
        for char in input_str:
            if char.isalpha():
                fruit_name += char
            else:
                break
        return fruit_name
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(extract_fruit_name('apples30'))  # Output: apples
print(extract_fruit_name('peaches24'))  # Output: peaches
print(extract_fruit_name('peaches0'))  # Output: peaches
print(extract_fruit_name('pears'))  # Output: pears

# End time: 2024-03-30 21:17:26.073736
# Elapsed time in seconds: 2.8815709259997675