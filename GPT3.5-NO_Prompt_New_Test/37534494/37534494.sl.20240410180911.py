# Start time: 2024-04-10 18:13:02.716061

'''
Prompt:
Given that input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        sentence_list = input_list[:-1]
        keyword = input_list[-1]

        for sentence in sentence_list:
            if keyword in sentence:
                return sentence
    except:
        return "Invalid input"

# Test cases
print(generated_function('I love apples, I hate bananas, banana'))
print(generated_function('I love apples, I hate bananas, apple'))
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples

# End time: 2024-04-10 18:13:03.884253
# Elapsed time in seconds: 1.1681706449999183


# APPEND TEST SCRIPTS...
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples


print(generated_function("I like bananas", "I dislike apples", "apple"))  ### Output: I dislike apples
print(generated_function("I like bananas", "I dislike apples", "banana"))  ### Output: I like bananas

# TEST SCRIPTS APPENDED!

