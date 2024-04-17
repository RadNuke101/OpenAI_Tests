# Start time: 2024-04-10 13:40:24.956523

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word) is in the first input (expresssion), return true, else false, and input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function generated_function with two arguments
def generated_function(expression, word):
    # Check if the word is in the expression
    if word in expression:
        return True
    else:
        return False

# Test cases
print(generated_function('red ball, green sweater', 'red'))
print(generated_function('pink ball, green sweater', 'red'))
print(generated_function('blue sea, pink ribbon', 'red'))
print(generated_function('black sea, white ribbon', 'red'))
print(generated_function('red green blue', 'red'))
print(generated_function("red ball, green sweater", "red", "green", "pink"))  ## Output: true
print(generated_function("pink ball, green sweater", "red", "green", "pink"))  ## Output: false
print(generated_function("blue sea, pink ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("black sea, white ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("red green blue", "red", "blue", "pink"))  ## Output: true

# End time: 2024-04-10 13:40:26.648619
# Elapsed time in seconds: 1.6920625980001205