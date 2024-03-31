# Start time: 2024-03-30 23:42:46.337427

# Content: Given that given input as ['-%134'] output is %134, given input as ['500'] output is 500, given input as ['5.125'] output is 5.125, given input as ['-%43.00'] output is %43.00, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '-%134', output: %134
# input: '500', output: 500
# input: '5.125', output: 5.125
# input: '-%43.00', output: %43.00

def process_input(input_str):
    try:
        if input_str[0] == '-':
            input_str = input_str[1:]
        if '.' in input_str:
            return float(input_str)
        else:
            return int(input_str)
    except ValueError:
        return "Invalid input"

# Test the function with the provided test cases
print(process_input('-%134'))
print(process_input('500'))
print(process_input('5.125'))
print(process_input('-%43.00'))

# End time: 2024-03-30 23:42:48.157501
# Elapsed time in seconds: 1.8200457409984665