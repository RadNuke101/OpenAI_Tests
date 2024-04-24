# Start time: 2024-04-05 18:34:12.762541

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false, and input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(sentence, word1, word2, word3):
    # Split the sentence to work with individual words
    words = sentence.split()
    
    # Check if only one of the words from the second, third, or fourth column
    # is in the first two words of the sentence
    match_count = 0
    for word in words[:2]:  # Only consider the first two words of the sentence
        if word in [word1, word2, word3]:
            match_count += 1
    
    # Return true if exactly one match is found, else false
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

# End time: 2024-04-05 18:34:20.652142
# Elapsed time in seconds: 7.889452412999162


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

