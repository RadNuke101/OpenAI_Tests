# Start time: 2024-03-30 20:44:01.887479

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def find_matching_sentence(input_str):
    try:
        input_list = input_str.split(',')
        sentences = input_list[:-1]
        keyword = input_list[-1].strip()

        for sentence in sentences:
            if keyword in sentence:
                return sentence.strip()

        return "No matching sentence found"

    except Exception as e:
        return "Error: Invalid input format"

# Test cases
"""
['I love apples', 'I hate bananas', 'banana']
['I love apples', 'I hate bananas', 'apple']
"""

# End time: 2024-03-30 20:44:03.420906
# Elapsed time in seconds: 1.5333865370002968