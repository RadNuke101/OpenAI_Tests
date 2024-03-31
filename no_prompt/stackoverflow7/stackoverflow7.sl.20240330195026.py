# Start time: 2024-03-30 20:04:58.049275

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_item(input_str):
    try:
        # Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
        # Output: Item 1
        if 'Item' in input_str:
            return input_str.split(' ')[0]
        
        # Input: 'Item 2 AQ-230A-1DUQ', 'AQ-230A'
        # Output: Item 2 -1DUQ
        else:
            item_num = input_str.split(' ')[0]
            item_code = input_str.split(' ')[1]
            return f'{item_num} {item_code}'
    
    except Exception as e:
        print(f'Error: {e}')

# Test cases
print(extract_item('Item 1 AQ-S810W-2AVDF'))  # Expected output: Item 1
print(extract_item('Item 2 AQ-230A-1DUQ'))    # Expected output: Item 2 -1DUQ

# End time: 2024-03-30 20:05:00.504504
# Elapsed time in seconds: 2.4564340529996116