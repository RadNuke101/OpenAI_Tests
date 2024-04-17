# Start time: 2024-04-10 15:17:29.962821

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1: The input column contains phrases or sentences.

Summary for Input Column 2: The input column contains single words.

Summary for Output Column: The output column contains boolean values (true or false).

Relationship Summary: The output is true when the word in Input Column 2 is found in the corresponding phrase or sentence in Input Column 1. Otherwise, the output is false. The relationship between the input and output is based on whether the word in Input Column 2 is present in the corresponding phrase or sentence in Input Column 1., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phrase, word):
    # Check if the word is present in the phrase
    if word in phrase:
        return True
    else:
        return False

# Test cases
print(generated_function('An apple a day keeps the doctor away', 'apple'))
print(generated_function('An apple a day keeps the doctor away', 'orange'))
print(generated_function('Better the devil you know', 'you know'))
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-10 15:17:31.584557
# Elapsed time in seconds: 1.6217002719999982