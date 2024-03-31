# Start time: 2024-03-30 22:12:54.922470

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_input_output(input_str):
    try:
        # Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
        # Output: Item 1
        input_parts = input_str.split(', ')
        if len(input_parts) != 2:
            raise ValueError("Input format is incorrect")
        
        if input_parts[0].startswith('Item'):
            output = input_parts[0]
        else:
            output = input_parts[1]
        
        return output

    except Exception as e:
        return str(e)

# Test cases
print(match_input_output('Item 1 AQ-S810W-2AVDF, AQ-S810W-2AVDF'))  # Output: Item 1
print(match_input_output('Item 2 AQ-230A-1DUQ, AQ-230A'))  # Output: Item 2 -1DUQ

# End time: 2024-03-30 22:12:57.231988
# Elapsed time in seconds: 2.3106866759990226