# Start time: 2024-03-30 21:57:12.055626

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
# Output: Item 1

# Input: 'Item 2 AQ-230A-1DUQ', 'AQ-230A'
# Output: Item 2 -1DUQ

def match_input_output(input_str, output_str):
    try:
        input_parts = input_str.split(' ')
        output_parts = output_str.split(' ')

        if input_parts[-1] == output_parts[-1]:
            return ' '.join(input_parts[:-1])
        else:
            return ' '.join(input_parts)
    except:
        return "Invalid input or output format"

# Test cases
print(match_input_output('Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'))  # Output: Item 1
print(match_input_output('Item 2 AQ-230A-1DUQ', 'AQ-230A'))  # Output: Item 2 -1DUQ

# End time: 2024-03-30 21:57:14.281973
# Elapsed time in seconds: 2.2263502690002497