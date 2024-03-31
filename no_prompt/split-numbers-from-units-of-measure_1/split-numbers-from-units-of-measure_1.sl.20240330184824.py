# Start time: 2024-03-30 18:56:44.007244

# Content: Given that given input as ['80v', '3'] output is 80, given input as ['10hrs', '3'] output is 10, given input as ['7h', '2'] output is 7, given input as ['500m', '4'] output is 500, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# input: '80v', '3'
# output: 80
# input: '10hrs', '3'
# output: 10
# input: '7h', '2'
# output: 7
# input: '500m', '4'
# output: 500

def extract_number(input_str):
    number = ''
    for char in input_str:
        if char.isdigit():
            number += char
        else:
            break
    return int(number)

try:
    input_str1 = '80v'
    input_str2 = '3'
    output1 = extract_number(input_str1)
    print(output1)

    input_str1 = '10hrs'
    input_str2 = '3'
    output2 = extract_number(input_str1)
    print(output2)

    input_str1 = '7h'
    input_str2 = '2'
    output3 = extract_number(input_str1)
    print(output3)

    input_str1 = '500m'
    input_str2 = '4'
    output4 = extract_number(input_str1)
    print(output4)

except ValueError:
    print("Invalid input. Please provide a valid input.")

# End time: 2024-03-30 18:56:48.241538
# Elapsed time in seconds: 4.234189256000036