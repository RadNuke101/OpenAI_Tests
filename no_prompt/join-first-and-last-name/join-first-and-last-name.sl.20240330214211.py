# Start time: 2024-03-30 21:55:33.914181

# Content: Given that given input as ['susan', 'chang'] output is susan chang, given input as ['aaron', 'kim'] output is aaron kim, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def combine_names(input_str):
    try:
        names = input_str.split(',')
        first_name = names[0].strip()
        last_name = names[1].strip()
        return first_name + ' ' + last_name
    except Exception as e:
        return "Invalid input format. Please provide two names separated by a comma."

# Test cases
# input: 'susan, chang'
# output: 'susan chang'
print(combine_names('susan, chang'))

# input: 'aaron, kim'
# output: 'aaron kim'
print(combine_names('aaron, kim'))

# End time: 2024-03-30 21:55:35.403838
# Elapsed time in seconds: 1.489602632000242