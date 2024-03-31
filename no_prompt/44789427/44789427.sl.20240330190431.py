# Start time: 2024-03-30 19:15:36.604543

# Content: Given that given input as ['1/17/16-1/18/17', '1'] output is 1/17/16, given input as ['1/17/16-1/18/17', '2'] output is 1/18/17, given input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, given input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date(input_str, num):
    try:
        date_range, index = input_str.split('-'), int(num)
        start_date, end_date = date_range[0], date_range[1]
        
        if index == 1:
            return start_date
        elif index == 2:
            return end_date
        else:
            return "Invalid index"
    
    except ValueError:
        return "Invalid input format"

# Test cases
"""
print(extract_date('1/17/16-1/18/17', '1'))  # Output should be 1/17/16
print(extract_date('1/17/16-1/18/17', '2'))  # Output should be 1/18/17
print(extract_date('01/17/2016-01/18/2017', '1'))  # Output should be 01/17/2016
print(extract_date('01/17/2016-01/18/2017', '2'))  # Output should be 01/18/2017
"""

# End time: 2024-03-30 19:15:39.687987
# Elapsed time in seconds: 3.0833548450000308