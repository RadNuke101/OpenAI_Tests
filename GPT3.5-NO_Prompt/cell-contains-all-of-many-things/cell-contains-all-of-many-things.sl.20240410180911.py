# Start time: 2024-04-10 18:19:48.387558

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        sentence = input_list[0]
        words = input_list[1:]

        for word in words:
            if word not in sentence:
                return False

        return True
    except:
        return False

# Test cases
print(generated_function('yellow dog on green grass, yellow, green, dog'))
print(generated_function('Lone dog with a green frisbie on yellow sand, yellow, green, dog'))
print(generated_function('A yellow sun in a green field, yellow, green, dog'))
print(generated_function('yellow neon sign with a green background, yellow, green, dog'))
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("Lone dog with a green frisbie on yellow sand", "yellow", "green", "dog"))  ## Output: true
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: false
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: false

# End time: 2024-04-10 18:19:52.429742
# Elapsed time in seconds: 4.042088861000138