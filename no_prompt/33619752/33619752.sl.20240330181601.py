# Start time: 2024-03-30 18:25:24.933860

# Content: Given that given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_company_name(input_str):
    try:
        input_str = input_str.replace('[', '').replace(']', '')  # Remove brackets if present
        words = input_str.split()  # Split input string into words
        if 'Inc' in words:
            return ' '.join(words[:words.index('Inc')])  # Return words before 'Inc'
        elif 'Corporation' in words:
            return ' '.join(words[:words.index('Corporation')])  # Return words before 'Corporation'
        else:
            return input_str  # Return input string as is
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
"""
Input: 'General Electric'
Output: 'General Electric'

Input: 'General Electric Inc'
Output: 'General Electric'

Input: 'General Electric Company'
Output: 'General Electric'

Input: 'Microsoft'
Output: 'Microsoft'

Input: 'Microsoft Corporation'
Output: 'Microsoft'

Input: 'Nintendo'
Output: 'Nintendo'

Input: 'Nintendo Enterprises'
Output: 'Nintendo'
"""

# End time: 2024-03-30 18:25:27.117412
# Elapsed time in seconds: 2.183529830999987