# Start time: 2024-03-30 21:01:07.444526

# Content: Given that given input as ['The'] output is 3, given input as ['The quick fox'] output is 13, given input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'The' , Output: 3
# Input: 'The quick fox' , Output: 13
# Input: 'The quick  fox' , Output: 14

def count_characters(input_str):
    try:
        # Remove extra whitespaces and split the input string into words
        words = input_str.split()
        
        # Count the total number of characters in the words
        total_chars = sum(len(word) for word in words)
        
        return total_chars
    except Exception as e:
        print("Error:", e)

# Test cases
print(count_characters('The'))  # Output: 3
print(count_characters('The quick fox'))  # Output: 13
print(count_characters('The quick  fox'))  # Output: 14

# End time: 2024-03-30 21:01:12.242646
# Elapsed time in seconds: 4.7979889739999635