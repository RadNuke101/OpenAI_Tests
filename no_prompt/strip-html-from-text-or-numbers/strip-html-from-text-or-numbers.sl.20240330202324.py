# Start time: 2024-03-30 20:39:06.768144

# Content: Given that given input as ['<b>0.66<b>'] output is 0.66, given input as ['<b>0.409<b>'] output is 0.409, given input as ['<b>0.7268<b>'] output is 0.7268, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_str):
    try:
        start_index = input_str.find('<b>') + 3
        end_index = input_str.find('<', start_index)
        number = float(input_str[start_index:end_index])
        return number
    except ValueError:
        print("Error: Unable to extract number from input")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Test cases
input_str1 = '<b>0.66<b>'
input_str2 = '<b>0.409<b>'
input_str3 = '<b>0.7268<b>'

output1 = extract_number(input_str1)
output2 = extract_number(input_str2)
output3 = extract_number(input_str3)

# End time: 2024-03-30 20:39:09.731580
# Elapsed time in seconds: 2.96335950699995