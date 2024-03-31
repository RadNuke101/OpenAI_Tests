# Start time: 2024-03-30 19:12:25.156903

# Content: Given that given input as ['Jones <60>'] output is 60, given input as ['Jones <57>'] output is 57, given input as ['Jones <55>'] output is 55, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'Jones <60>', output: 60
# input: 'Jones <57>', output: 57
# input: 'Jones <55>', output: 55

def extract_number(input_str):
    try:
        # Find the index of '<' and '>'
        start_index = input_str.find('<')
        end_index = input_str.find('>')
        
        # Extract the number between '<' and '>'
        number = int(input_str[start_index+1:end_index])
        
        return number
    except ValueError:
        print("Error: Invalid input format. Number not found.")
    except Exception as e:
        print("An error occurred:", e)

# Test the function with the provided test cases
print(extract_number('Jones <60>'))
print(extract_number('Jones <57>'))
print(extract_number('Jones <55>'))

# End time: 2024-03-30 19:12:27.787113
# Elapsed time in seconds: 2.630130559999998