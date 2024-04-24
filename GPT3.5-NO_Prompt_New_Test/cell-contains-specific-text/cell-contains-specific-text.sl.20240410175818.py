# Start time: 2024-04-10 18:01:25.306905

'''
Prompt:
Given that input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        sentence = input_list[0].strip()
        word = input_list[1].strip()

        return word in sentence
    except Exception as e:
        return False

# Test cases
print(generated_function('An apple a day keeps the doctor away, apple'))
print(generated_function('An apple a day keeps the doctor away, orange'))
print(generated_function('Better the devil you know, you know'))
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-10 18:01:26.565179
# Elapsed time in seconds: 1.2582769360001294


# APPEND TEST SCRIPTS...
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true


print(generated_function("A banana a day keeps the doctor away.", "orange"))  ### Output: [
print(generated_function("Better the devil you know", "devil"))  ### Output: f
print(generated_function("A banana a day keeps the doctor away.", "banana"))  ### Output: a
print(generated_function("A banana a day keeps the doctor away.", "doctor"))  ### Output: l

# TEST SCRIPTS APPENDED!

