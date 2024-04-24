# Start time: 2024-04-05 18:00:48.459422

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(sentence, word1, word2, word3):
    # Split the first input to get the first two words
    first_two_words = sentence.split()[:2]
    # Initialize a counter for matches
    match_count = 0
    
    # Check each of the next three inputs if they are in the first two words
    if word1 in first_two_words:
        match_count += 1
    if word2 in first_two_words:
        match_count += 1
    if word3 in first_two_words:
        match_count += 1
    
    # If exactly one of the inputs from the second, third, or fourth column is in the first two words, return true
    return match_count == 1

# Test cases
print(generated_function('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Expected output: True
print(generated_function('warm gray sweater', 'yellow', 'green', 'cat'))  # Expected output: False
print(generated_function('blue neon signs', 'blue', 'green', 'neon'))  # Expected output: False
print(generated_function('hot pink socks', 'blue', 'pink', 'neon'))  # Expected output: True
print(generated_function('deep black eyes', 'yellow', 'green', 'neon'))  # Expected output: False
print(generated_function("yellow dog on green grass", "yellow", "green", "cat"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "cat"))  ## Output: false
print(generated_function("blue neon signs", "blue", "green", "neon"))  ## Output: false
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ## Output: true
print(generated_function("deep black eyes", "yellow", "green", "neon"))  ## Output: false

# End time: 2024-04-05 18:00:55.652517
# Elapsed time in seconds: 7.192878673999985


# APPEND TEST SCRIPTS...
print(generated_function("yellow dog on green grass", "yellow", "green", "cat"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "cat"))  ## Output: false
print(generated_function("blue neon signs", "blue", "green", "neon"))  ## Output: false
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ## Output: true
print(generated_function("deep black eyes", "yellow", "green", "neon"))  ## Output: false


print(generated_function("deep black eyes", "red", "green", "neon"))  ### Output: [
print(generated_function("red dog on green grass", "red", "green", "cat"))  ### Output: f
print(generated_function("warm white sweater", "red", "green", "cat"))  ### Output: a
print(generated_function("blue neon signs", "blue", "green", "neon"))  ### Output: l
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ### Output: s

# TEST SCRIPTS APPENDED!

