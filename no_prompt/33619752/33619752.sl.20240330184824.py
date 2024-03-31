# Start time: 2024-03-30 18:58:21.915845

# Content: Given that given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_company_name(input_str):
    try:
        input_str = input_str[0]  # Convert list input to string
    except TypeError:
        pass

    # Remove common suffixes from company names
    if input_str.endswith(' Inc') or input_str.endswith(' Corporation') or input_str.endswith(' Company') or input_str.endswith(' Enterprises'):
        input_str = input_str.rsplit(' ', 1)[0]

    return input_str

# Test cases
"""
Input: 'General Electric'
Output: 'General Electric'
"""
print(clean_company_name('General Electric'))

"""
Input: 'General Electric Inc'
Output: 'General Electric'
"""
print(clean_company_name('General Electric Inc'))

"""
Input: 'General Electric Company'
Output: 'General Electric'
"""
print(clean_company_name('General Electric Company'))

"""
Input: 'Microsoft'
Output: 'Microsoft'
"""
print(clean_company_name('Microsoft'))

"""
Input: 'Microsoft Corporation'
Output: 'Microsoft'
"""
print(clean_company_name('Microsoft Corporation'))

"""
Input: 'Nintendo'
Output: 'Nintendo'
"""
print(clean_company_name('Nintendo'))

"""
Input: 'Nintendo Enterprises'
Output: 'Nintendo'
"""
print(clean_company_name('Nintendo Enterprises'))

# End time: 2024-03-30 18:58:24.353209
# Elapsed time in seconds: 2.4372920480000175