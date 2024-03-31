# Start time: 2024-03-30 19:39:48.914456

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_input_output(input_str):
    try:
        input_list = input_str.split(', ')
        sentence1 = input_list[0]
        sentence2 = input_list[1]
        keyword = input_list[2]

        if keyword in sentence1:
            return sentence1
        elif keyword in sentence2:
            return sentence2
        else:
            return "Keyword not found in any sentence"
    
    except IndexError:
        return "Input format is incorrect. Please provide 3 strings separated by commas and spaces."
    except Exception as e:
        return str(e)

# Test cases
"""
Input: 'I love apples, I hate bananas, banana'
Output: 'I hate bananas'
"""
print(match_input_output('I love apples, I hate bananas, banana'))

"""
Input: 'I love apples, I hate bananas, apple'
Output: 'I love apples'
"""
print(match_input_output('I love apples, I hate bananas, apple'))

"""
Input: 'I love apples, I hate bananas'
Output: 'Input format is incorrect. Please provide 3 strings separated by commas and spaces.'
"""
print(match_input_output('I love apples, I hate bananas'))

"""
Input: 'I love apples, I hate bananas, apple, banana'
Output: 'Input format is incorrect. Please provide 3 strings separated by commas and spaces.'
"""
print(match_input_output('I love apples, I hate bananas, apple, banana'))

# End time: 2024-03-30 19:39:52.535902
# Elapsed time in seconds: 3.6214101069999742