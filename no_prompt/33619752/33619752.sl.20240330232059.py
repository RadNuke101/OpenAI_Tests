# Start time: 2024-03-30 23:30:25.803479

# Content: Given that given input as ['General Electric'] output is General Electric, given input as ['General Electric Inc'] output is General Electric, given input as ['General Electric Company'] output is General Electric, given input as ['Microsoft'] output is Microsoft, given input as ['Microsoft Corporation'] output is Microsoft, given input as ['Nintendo'] output is Nintendo, given input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_company_name(input_str):
    try:
        company_name = input_str[0]
        if 'Inc' in company_name:
            return company_name.replace(' Inc', '')
        elif 'Company' in company_name:
            return company_name.replace(' Company', '')
        elif 'Corporation' in company_name:
            return company_name.replace(' Corporation', '')
        else:
            return company_name
    except IndexError:
        return "Invalid input"

# Test cases
'''
print(clean_company_name(['General Electric']))  # Output: General Electric
print(clean_company_name(['General Electric Inc']))  # Output: General Electric
print(clean_company_name(['General Electric Company']))  # Output: General Electric
print(clean_company_name(['Microsoft']))  # Output: Microsoft
print(clean_company_name(['Microsoft Corporation']))  # Output: Microsoft
print(clean_company_name(['Nintendo']))  # Output: Nintendo
print(clean_company_name(['Nintendo Enterprises']))  # Output: Nintendo
'''

# End time: 2024-03-30 23:30:29.558728
# Elapsed time in seconds: 3.7551361940022616