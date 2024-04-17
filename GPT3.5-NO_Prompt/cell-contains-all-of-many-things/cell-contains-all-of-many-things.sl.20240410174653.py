# Start time: 2024-04-10 17:57:00.838893

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        sentence = input_list[0]
        keywords = input_list[1:]
        
        for keyword in keywords:
            if keyword not in sentence:
                return False
        
        return True
    except Exception as e:
        return "Error: Invalid input format"

# Test cases
print(generated_function('yellow dog on green grass, yellow, green, dog'))
print(generated_function('Lone dog with a green frisbie on yellow sand, yellow, green, dog'))
print(generated_function('A yellow sun in a green field, yellow, green, dog'))
print(generated_function('yellow neon sign with a green background, yellow, green, dog'))
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("Lone dog with a green frisbie on yellow sand", "yellow", "green", "dog"))  ## Output: true
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: false
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: false

# End time: 2024-04-10 17:57:03.348722
# Elapsed time in seconds: 2.5097621559998515