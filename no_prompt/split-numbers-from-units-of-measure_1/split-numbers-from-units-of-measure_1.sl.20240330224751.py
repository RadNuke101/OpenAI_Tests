# Start time: 2024-03-30 22:57:11.966200

# Content: Given that given input as ['80v', '3'] output is 80, given input as ['10hrs', '3'] output is 10, given input as ['7h', '2'] output is 7, given input as ['500m', '4'] output is 500, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '80v', '3'
# Output: 80

# Input: '10hrs', '3'
# Output: 10

# Input: '7h', '2'
# Output: 7

# Input: '500m', '4'
# Output: 500

def extract_number(input_str):
    num = ''
    for char in input_str:
        if char.isdigit():
            num += char
        else:
            break
    return int(num)

try:
    input_str1 = '80v'
    output1 = extract_number(input_str1)
    print(output1)

    input_str2 = '10hrs'
    output2 = extract_number(input_str2)
    print(output2)

    input_str3 = '7h'
    output3 = extract_number(input_str3)
    print(output3)

    input_str4 = '500m'
    output4 = extract_number(input_str4)
    print(output4)
except:
    print("Error: Invalid input")

# End time: 2024-03-30 22:57:16.595843
# Elapsed time in seconds: 4.629537775999779