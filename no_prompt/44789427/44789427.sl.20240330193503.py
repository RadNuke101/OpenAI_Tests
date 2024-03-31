# Start time: 2024-03-30 19:46:22.713027

# Content: Given that given input as ['1/17/16-1/18/17', '1'] output is 1/17/16, given input as ['1/17/16-1/18/17', '2'] output is 1/18/17, given input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, given input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date(input_str, index):
    # Input: '1/17/16-1/18/17', '1'
    # Output: 1/17/16
    # Input: '1/17/16-1/18/17', '2'
    # Output: 1/18/17
    # Input: '01/17/2016-01/18/2017', '1'
    # Output: 01/17/2016
    # Input: '01/17/2016-01/18/2017', '2'
    # Output: 01/18/2017
    
    try:
        dates = input_str.split('-')
        if index == '1':
            return dates[0]
        elif index == '2':
            return dates[1]
        else:
            return "Invalid index"
    except IndexError:
        return "Invalid input format"

# Test cases
print(extract_date('1/17/16-1/18/17', '1'))
print(extract_date('1/17/16-1/18/17', '2'))
print(extract_date('01/17/2016-01/18/2017', '1'))
print(extract_date('01/17/2016-01/18/2017', '2'))

# End time: 2024-03-30 19:46:26.354611
# Elapsed time in seconds: 3.64154381499975