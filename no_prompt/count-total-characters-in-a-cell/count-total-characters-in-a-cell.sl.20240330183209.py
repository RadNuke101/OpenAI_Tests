# Start time: 2024-03-30 18:39:01.766794

# Content: Given that given input as ['The'] output is 3, given input as ['The quick fox'] output is 13, given input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'The', output: 3
# input: 'The quick fox', output: 13
# input: 'The quick  fox', output: 14

def calculate_length(input_str):
    try:
        # Split the input string by spaces
        words = input_str.split()
        
        # Calculate the total length of all words
        total_length = sum(len(word) for word in words)
        
        return total_length
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function with the provided test cases
print(calculate_length('The'))
print(calculate_length('The quick fox'))
print(calculate_length('The quick  fox'))

# End time: 2024-03-30 18:39:03.801548
# Elapsed time in seconds: 2.034696767000014