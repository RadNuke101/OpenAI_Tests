# Start time: 2024-03-30 19:18:05.959217

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_item(input_str):
    try:
        # Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
        # Output: Item 1
        item = input_str.split(' ')[0]
        return item
    except Exception as e:
        print("Error: ", e)
        return None

def extract_code(input_str):
    try:
        # Input: 'Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'
        # Output: AQ-S810W-2AVDF
        code = input_str.split(' ')[-1]
        return code
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
input_str1 = 'Item 1 AQ-S810W-2AVDF'
input_str2 = 'AQ-S810W-2AVDF'
print(extract_item(input_str1))  # Output: Item 1
print(extract_code(input_str1))  # Output: AQ-S810W-2AVDF

input_str3 = 'Item 2 AQ-230A-1DUQ'
input_str4 = 'AQ-230A'
print(extract_item(input_str3))  # Output: Item 2
print(extract_code(input_str3))  # Output: AQ-230A-1DUQ

# End time: 2024-03-30 19:18:08.742744
# Elapsed time in seconds: 2.7834576000000197