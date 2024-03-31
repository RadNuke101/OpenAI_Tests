# Start time: 2024-03-30 19:14:12.207343

# Content: Given that given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_company_name(company_name):
    try:
        company_name = company_name.replace(' Inc', '').replace(' Company', '').replace(' Corporation', '')
        return company_name
    except AttributeError:
        print("Invalid input. Please provide a valid company name as a string.")

# Test cases
"""
print(clean_company_name('General Electric'))  # Output: General Electric
print(clean_company_name('General Electric Inc'))  # Output: General Electric
print(clean_company_name('General Electric Company'))  # Output: General Electric
print(clean_company_name('Microsoft'))  # Output: Microsoft
print(clean_company_name('Microsoft Corporation'))  # Output: Microsoft
print(clean_company_name('Nintendo'))  # Output: Nintendo
print(clean_company_name('Nintendo Enterprises'))  # Output: Nintendo
"""

# End time: 2024-03-30 19:14:13.644172
# Elapsed time in seconds: 1.4367846540003484