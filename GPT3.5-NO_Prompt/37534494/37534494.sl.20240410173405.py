# Start time: 2024-04-10 17:38:28.134931

'''
Prompt:
Given that input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        if input_list[2] in input_list[0]:
            return input_list[0]
        elif input_list[2] in input_list[1]:
            return input_list[1]
    except IndexError:
        return "Input format is incorrect. Please provide three strings separated by commas and spaces."
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('I love apples, I hate bananas, banana'))
print(generated_function('I love apples, I hate bananas, apple'))
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples

# End time: 2024-04-10 17:38:30.513028
# Elapsed time in seconds: 2.3780758660000174