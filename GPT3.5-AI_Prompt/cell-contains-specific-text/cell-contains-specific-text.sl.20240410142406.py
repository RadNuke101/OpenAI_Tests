# Start time: 2024-04-10 14:30:24.490680

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The first input column contains phrases or sentences.
- The second input column contains specific words or terms.

Summary for Output Column Data:
- The output column contains boolean values (true or false) indicating whether the second input term is present in the corresponding phrase or sentence from the first input column.

Relationship Summary:
- The relationship between the input and output columns is based on whether the specific word or term from the second input column is present in the corresponding phrase or sentence from the first input column. 
- If the word is present, the output is true; if not, the output is false.
- The output column serves as a way to determine the presence or absence of the specific term in each phrase or sentence., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phrase, term):
    # Check if the term is present in the phrase
    if term in phrase:
        return True
    else:
        return False

# Test cases
print(generated_function('An apple a day keeps the doctor away', 'apple'))  # Output: True
print(generated_function('An apple a day keeps the doctor away', 'orange'))  # Output: False
print(generated_function('Better the devil you know', 'you know'))  # Output: True
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-10 14:30:26.325102
# Elapsed time in seconds: 1.8343839369999841