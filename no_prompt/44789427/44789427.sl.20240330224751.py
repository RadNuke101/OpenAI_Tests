# Start time: 2024-03-30 23:00:18.198012

# Content: Given that given input as ['1/17/16-1/18/17', '1'] output is 1/17/16, given input as ['1/17/16-1/18/17', '2'] output is 1/18/17, given input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, given input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date(input_str, num):
    try:
        dates = input_str.split('-')
        if num == '1':
            return dates[0]
        elif num == '2':
            return dates[1]
        else:
            return "Invalid input for number"
    except IndexError:
        return "Invalid input format"

# Test cases
# input: '1/17/16-1/18/17', '1' => output: '1/17/16'
# input: '1/17/16-1/18/17', '2' => output: '1/18/17'
# input: '01/17/2016-01/18/2017', '1' => output: '01/17/2016'
# input: '01/17/2016-01/18/2017', '2' => output: '01/18/2017'

# End time: 2024-03-30 23:00:20.932541
# Elapsed time in seconds: 2.7344714449991443