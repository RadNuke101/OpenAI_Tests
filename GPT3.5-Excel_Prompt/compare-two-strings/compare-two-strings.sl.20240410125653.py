# Start time: 2024-04-10 12:58:16.528962

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if both the first and second inputs match exactly, including capitalization, return true, else false, and input as ['apple', 'apple'] output is true, input as ['orange', 'Orange'] output is false, input as ['peach', 'peach'] output is true, input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function
def generated_function(input1, input2):
    # Check if the inputs match exactly, including capitalization
    if input1 == input2:
        return True
    else:
        return False

# Test cases
print(generated_function('apple', 'apple'))
print(generated_function('orange', 'Orange'))
print(generated_function('peach', 'peach'))
print(generated_function('cherry', 'cherrY'))
print(generated_function("apple", "apple"))  ## Output: true
print(generated_function("orange", "Orange"))  ## Output: false
print(generated_function("peach", "peach"))  ## Output: true
print(generated_function("cherry", "cherrY"))  ## Output: false

# End time: 2024-04-10 12:58:18.866922
# Elapsed time in seconds: 2.337919929000009