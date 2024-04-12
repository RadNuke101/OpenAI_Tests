# Start time: 2024-04-05 18:37:56.329492

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the last word of the inputted phrase, and input as ['focus on one thing at a time'] output is time, input as ['premature opt is the root of all evil'] output is evil, input as ['where is life'] output is life, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the last word
    return phrase.split()[-1]

# Test cases
result1 = generated_function('focus on one thing at a time')
result2 = generated_function('premature opt is the root of all evil')
result3 = generated_function('where is life')
print(generated_function("focus on one thing at a time"))  ## Output: time
print(generated_function("premature opt is the root of all evil"))  ## Output: evil
print(generated_function("where is life"))  ## Output: life

# End time: 2024-04-05 18:37:58.963848
# Elapsed time in seconds: 2.634306187999755