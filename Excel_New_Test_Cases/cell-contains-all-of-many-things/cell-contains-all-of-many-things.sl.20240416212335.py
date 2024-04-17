# Start time: 2024-04-16 21:34:05.913527

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second, third, and fourth inputs (words) are in the first input (expression), then return true, else false, and input as: "yellow dog on green grass", "yellow", "green", "dog" output is: true, input as: "Lone dog with a green frisbie on yellow sand", "yellow", "green", "dog" output is: true, input as: "A yellow sun in a green field", "yellow", "green", "dog" output is: false, input as: "yellow neon sign with a green background", "yellow", "green", "dog" output is: false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str, word1, word2, word3):
    # Split the input string into words
    words = input_str.split()
    
    # Check if all three words are in the input expression
    if word1 in words and word2 in words and word3 in words:
        return 'true'
    else:
        return 'false'

# Test cases
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))
print(generated_function("Lone dog with a green frisbie on yellow sand", "yellow", "green", "dog"))
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))



print(generated_function("yellow dog-shaped neon sign with a green background", "yellow", "green", "dog"))  ### Output: "yellow dog-shaped neon sign with a green background", "yellow", "green", "dog"
print(generated_function("yellow dog on grass", "yellow", "green", "dog"))  ### Output: "yellow dog on grass", "yellow", "green", "dog"
print(generated_function("Lone cat with a green frisbie on yellow sand", "yellow", "green", "dog"))  ### Output: "Lone cat with a green frisbie on yellow sand", "yellow", "green", "dog"
print(generated_function("A yellow sun in a green field with a dog walking around", "yellow", "green", "dog"))  ### Output: "A yellow sun in a green field with a dog walking around", "yellow", "green", "dog"


print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("Lone dog with a green frisbie on yellow sand", "yellow", "green", "dog"))  ## Output: true
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: false
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: false



# End time: 2024-04-16 21:34:08.467156
# Elapsed time in seconds: 2.5535746159999917