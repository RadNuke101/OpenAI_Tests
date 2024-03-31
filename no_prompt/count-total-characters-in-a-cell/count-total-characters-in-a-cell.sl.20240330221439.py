# Start time: 2024-03-30 22:21:25.181726

# Content: Given that given input as ['The'] output is 3, given input as ['The quick fox'] output is 13, given input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'The'  Output: 3
# Input: 'The quick fox'  Output: 13
# Input: 'The quick  fox'  Output: 14

def count_characters(input_str):
    try:
        # Remove extra spaces and split the input string into words
        words = input_str.split()
        
        # Count the total number of characters in the words
        total_chars = sum(len(word) for word in words)
        
        return total_chars
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function with the provided test cases
print(count_characters('The'))
print(count_characters('The quick fox'))
print(count_characters('The quick  fox'))

# End time: 2024-03-30 22:21:28.280455
# Elapsed time in seconds: 3.0986411390003923