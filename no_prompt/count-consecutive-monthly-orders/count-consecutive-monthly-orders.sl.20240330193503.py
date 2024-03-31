# Start time: 2024-03-30 19:45:02.557196

# Content: Given that given input as ['7 0 0 5 4 4'] output is 3, given input as ['0 0 2 3 3 0'] output is 3, given input as ['5 6 4 6 0 7'] output is 4, given input as ['0 4 5 0 0 2'] output is 2, given input as ['3 0 3 0 1 2'] output is 2, given input as ['5 3 2 5 6 1'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '7 0 0 5 4 4', output: '3'
# input: '0 0 2 3 3 0', output: '3'
# input: '5 6 4 6 0 7', output: '4'
# input: '0 4 5 0 0 2', output: '2'
# input: '3 0 3 0 1 2', output: '2'
# input: '5 3 2 5 6 1', output: '6'

def find_unique_number(input_str):
    try:
        nums = list(map(int, input_str.split()))
        unique_num = None
        for num in nums:
            if nums.count(num) == 1:
                unique_num = num
                break
        return unique_num
    except ValueError:
        return "Invalid input. Please provide a string of space-separated integers."

# Test the function with the provided test cases
print(find_unique_number('7 0 0 5 4 4'))
print(find_unique_number('0 0 2 3 3 0'))
print(find_unique_number('5 6 4 6 0 7'))
print(find_unique_number('0 4 5 0 0 2'))
print(find_unique_number('3 0 3 0 1 2'))
print(find_unique_number('5 3 2 5 6 1'))

# End time: 2024-03-30 19:45:05.660656
# Elapsed time in seconds: 3.103426469000624