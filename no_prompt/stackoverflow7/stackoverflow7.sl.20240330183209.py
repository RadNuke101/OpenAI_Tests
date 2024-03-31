# Start time: 2024-03-30 18:47:00.043677

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_item(input_str):
    try:
        # Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
        # Output: Item 1
        parts = input_str.split(' ')
        return parts[0]
    except IndexError:
        return "Invalid input format"

def extract_code(input_str):
    try:
        # Input: 'Item 2 AQ-230A-1DUQ', 'AQ-230A'
        # Output: Item 2 -1DUQ
        parts = input_str.split(' ')
        if len(parts) == 3:
            return parts[1] + ' ' + parts[2]
        else:
            return "Invalid input format"
    except IndexError:
        return "Invalid input format"

# Test cases
print(extract_item('Item 1 AQ-S810W-2AVDF'))  # Output: Item 1
print(extract_code('Item 2 AQ-230A-1DUQ'))  # Output: Item 2 -1DUQ

# End time: 2024-03-30 18:47:04.029053
# Elapsed time in seconds: 3.9852715299999772