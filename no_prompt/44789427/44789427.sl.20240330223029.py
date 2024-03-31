# Start time: 2024-03-30 22:43:44.051391

# Content: Given that given input as ['1/17/16-1/18/17', '1'] output is 1/17/16, given input as ['1/17/16-1/18/17', '2'] output is 1/18/17, given input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, given input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date(input_str, num):
    try:
        date_range, index = input_str.split('-'), int(num)
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()
        
        if index == 1:
            return start_date
        elif index == 2:
            return end_date
        else:
            return "Invalid index, please enter 1 or 2"
    
    except ValueError:
        return "Invalid input format, please enter date range separated by '-' and index as a number"
    except IndexError:
        return "Invalid input format, please enter date range separated by '-' and index as a number"

# Test cases
# Input: '1/17/16-1/18/17', '1' => Output: '1/17/16'
# Input: '1/17/16-1/18/17', '2' => Output: '1/18/17'
# Input: '01/17/2016-01/18/2017', '1' => Output: '01/17/2016'
# Input: '01/17/2016-01/18/2017', '2' => Output: '01/18/2017'

# Uncomment the below lines to test the function
# print(extract_date('1/17/16-1/18/17', '1'))
# print(extract_date('1/17/16-1/18/17', '2'))
# print(extract_date('01/17/2016-01/18/2017', '1'))
# print(extract_date('01/17/2016-01/18/2017', '2'))

# End time: 2024-03-30 22:43:47.381671
# Elapsed time in seconds: 3.330176142999335