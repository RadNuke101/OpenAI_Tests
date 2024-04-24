# Start time: 2024-04-05 16:07:15.491944

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and input as ['011016_assignment.xlsx', '1'] output is 011016, input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, input as ['030116_cost.xlsx', '1'] output is 030116, input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(filename, n):
    # Convert n to integer
    n = int(n)
    # Split the filename by periods
    parts = filename.split('.')
    # Initialize variables to hold the result and the count of periods
    result = ""
    period_count = 0
    # Iterate over the characters in the filename
    for i, char in enumerate(filename):
        # Check if the character is a period
        if char == '.':
            period_count += 1
            # If the period count matches n, extract the substring
            if period_count == n:
                # If n is 1, extract from the start
                if n == 1:
                    result = filename[:i]
                # If n is greater than 1, extract between the nth and (n-1)th period
                else:
                    prev_period_index = filename.rfind('.', 0, i)
                    result = filename[prev_period_index+1:i]
                break
    # If n is 2 and period_count is 1, it means we need the substring after the last period
    if n == 2 and period_count == 1:
        result = parts[-1]
    return result

# Test cases
print(generated_function('011016_assignment.xlsx', '1'))  # Expected output: 011016
print(generated_function('011016_assignment.xlsx', '2'))  # Expected output: assignment.xlsx
print(generated_function('030116_cost.xlsx', '1'))  # Expected output: 030116
print(generated_function('030116_cost.xlsx', '2'))  # Expected output: cost.xlsx
print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx

# End time: 2024-04-05 16:07:30.589249
# Elapsed time in seconds: 15.096855063000021


# APPEND TEST SCRIPTS...
print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx


print(generated_function("011028_todosheet.xlsx", "1"))  ### Output: 011028
print(generated_function("030128_a.xlsx", "2"))  ### Output: a.xlsx
print(generated_function("030128_a.xlsx", "1"))  ### Output: 030128
print(generated_function("011028_todosheet.xlsx", "2"))  ### Output: todosheet.xlsx

# TEST SCRIPTS APPENDED!

