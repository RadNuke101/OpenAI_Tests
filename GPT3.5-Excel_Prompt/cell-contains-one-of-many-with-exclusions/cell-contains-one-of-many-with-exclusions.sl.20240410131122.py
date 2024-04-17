# Start time: 2024-04-10 13:23:27.060063

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function
def generated_function(input_str, word1, word2, word3):
    # Split the input string into words
    words = input_str.split()
    
    # Check if only one of the inputs is in the first two words of the input string
    count = 0
    if word1 in words[:2]:
        count += 1
    if word2 in words[:2]:
        count += 1
    if word3 in words[:2]:
        count += 1
    
    return count == 1

# Test cases
generated_function('yellow dog on green grass', 'yellow', 'green', 'cat')
generated_function('warm gray sweater', 'yellow', 'green', 'cat')
generated_function('blue neon signs', 'blue', 'green', 'neon')
generated_function('hot pink socks', 'blue', 'pink', 'neon')
generated_function('deep black eyes', 'yellow', 'green', 'neon')
print(generated_function("yellow dog on green grass", "yellow", "green", "cat"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "cat"))  ## Output: false
print(generated_function("blue neon signs", "blue", "green", "neon"))  ## Output: false
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ## Output: true
print(generated_function("deep black eyes", "yellow", "green", "neon"))  ## Output: false

# End time: 2024-04-10 13:23:31.411823
# Elapsed time in seconds: 4.351734727000121