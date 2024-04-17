# Start time: 2024-04-10 15:49:15.019516

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1:
- The input column 1 contains date ranges in the format of MM/DD/YY-MM/DD/YY or MM/DD/YYYY-MM/DD/YYYY.
- The dates in the input column are written in different formats, including with or without leading zeros for the month and day.

Summary for Input Column 2:
- The input column 2 contains numbers representing a specific day within the date range in column 1.
- The numbers in the input column 2 are likely used to indicate the start (1) or end (2) date of the range in column 1.

Summary for Output Column:
- The output column contains the specific date selected from the date range in column 1 based on the corresponding number in column 2.
- The output column displays the selected date in the same format as it appears in the input column 1.

Relationship between Input and Output:
- The input columns provide a range of dates, and the output column selects a specific date from that range based on the corresponding number in the input column 2.
- The output column serves as a way to extract a single date from the date range provided in the input column 1, allowing for easy reference to a specific point in time within that range., and input as ['1/17/16-1/18/17', '1'] output is 1/17/16, input as ['1/17/16-1/18/17', '2'] output is 1/18/17, input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(date_range, day_num):
    # Split the date range into start and end dates
    start_date, end_date = date_range.split('-')
    
    # Check if the year has 2 or 4 digits
    if len(start_date.split('/')[-1]) == 2:
        date_format = '%m/%d/%y'
    else:
        date_format = '%m/%d/%Y'
    
    # Convert the start and end dates to datetime objects
    start_date = datetime.datetime.strptime(start_date, date_format)
    end_date = datetime.datetime.strptime(end_date, date_format)
    
    # Select the specific date based on the day number
    if day_num == '1':
        selected_date = start_date.strftime(date_format)
    elif day_num == '2':
        selected_date = end_date.strftime(date_format)
    
    return selected_date

# Test cases
generated_function('1/17/16-1/18/17', '1')
generated_function('1/17/16-1/18/17', '2')
generated_function('01/17/2016-01/18/2017', '1')
generated_function('01/17/2016-01/18/2017', '2')
print(generated_function("1/17/16-1/18/17", "1"))  ## Output: 1/17/16
print(generated_function("1/17/16-1/18/17", "2"))  ## Output: 1/18/17
print(generated_function("01/17/2016-01/18/2017", "1"))  ## Output: 01/17/2016
print(generated_function("01/17/2016-01/18/2017", "2"))  ## Output: 01/18/2017

# End time: 2024-04-10 15:49:18.557939
# Elapsed time in seconds: 3.5383390309998504