# Start time: 2024-03-30 18:44:06.012674

# Content: Given that given input as ['1/17/16-1/18/17', '1'] output is 1/17/16, given input as ['1/17/16-1/18/17', '2'] output is 1/18/17, given input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, given input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_date_range(input_str, index):
    try:
        # Input: '1/17/16-1/18/17', '1'
        # Output: 1/17/16
        # Input: '1/17/16-1/18/17', '2'
        # Output: 1/18/17
        # Input: '01/17/2016-01/18/2017', '1'
        # Output: 01/17/2016
        # Input: '01/17/2016-01/18/2017', '2'
        # Output: 01/18/2017
        
        date_range, position = input_str.split('-')
        start_date, end_date = date_range.split('-')
        
        if index == '1':
            return start_date
        elif index == '2':
            return end_date
        else:
            return "Invalid index"
    
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(get_date_range('1/17/16-1/18/17', '1'))  # Output: 1/17/16
print(get_date_range('1/17/16-1/18/17', '2'))  # Output: 1/18/17
print(get_date_range('01/17/2016-01/18/2017', '1'))  # Output: 01/17/2016
print(get_date_range('01/17/2016-01/18/2017', '2'))  # Output: 01/18/2017

# End time: 2024-03-30 18:44:11.498596
# Elapsed time in seconds: 5.495570459000078