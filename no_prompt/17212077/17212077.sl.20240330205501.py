# Start time: 2024-03-30 21:09:04.572929

# Content: Given that given input as ['01/15/2013'] output is 01/2013, given input as ['03/07/2011'] output is 03/2011, given input as ['05/09/2009'] output is 05/2009, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_month_year(date_str):
    try:
        date_list = date_str.split('/')
        month_year = date_list[0] + '/' + date_list[2]
        return month_year
    except (IndexError, AttributeError, ValueError):
        return "Invalid date format"

# Test cases
"""
Input: '01/15/2013'
Output: '01/2013'
"""
print(extract_month_year('01/15/2013'))

"""
Input: '03/07/2011'
Output: '03/2011'
"""
print(extract_month_year('03/07/2011'))

"""
Input: '05/09/2009'
Output: '05/2009'
"""
print(extract_month_year('05/09/2009'))

# End time: 2024-03-30 21:09:06.621992
# Elapsed time in seconds: 2.0490171010005724