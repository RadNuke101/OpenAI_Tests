# Start time: 2024-03-30 20:46:59.145204

# Content: Given that given input as ['Jones <60>'] output is 60, given input as ['Jones <57>'] output is 57, given input as ['Jones <55>'] output is 55, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Jones <60>'
# Output: 60

# Input: 'Jones <57>'
# Output: 57

# Input: 'Jones <55>'
# Output: 55

def extract_number(input_str):
    try:
        start_index = input_str.find('<') + 1
        end_index = input_str.find('>')
        number = int(input_str[start_index:end_index])
        return number
    except ValueError:
        print("Error: Unable to extract number from input")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(extract_number('Jones <60>'))
print(extract_number('Jones <57>'))
print(extract_number('Jones <55>'))

# End time: 2024-03-30 20:47:02.243273
# Elapsed time in seconds: 3.0979852339996796