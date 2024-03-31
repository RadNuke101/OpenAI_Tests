# Start time: 2024-03-30 19:12:57.799854

# Content: Given that given input as ['80v', '3'] output is 80, given input as ['10hrs', '3'] output is 10, given input as ['7h', '2'] output is 7, given input as ['500m', '4'] output is 500, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '80v', '3'   output: 80
# input: '10hrs', '3' output: 10
# input: '7h', '2'    output: 7
# input: '500m', '4'  output: 500

def extract_number(input_str):
    try:
        num = ''
        for char in input_str:
            if char.isdigit():
                num += char
            else:
                break
        return int(num)
    except:
        return None

# Test the function with the provided test cases
print(extract_number('80v'))  # 80
print(extract_number('10hrs'))  # 10
print(extract_number('7h'))  # 7
print(extract_number('500m'))  # 500

# End time: 2024-03-30 19:12:59.683671
# Elapsed time in seconds: 1.8837547140001334