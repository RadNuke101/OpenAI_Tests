# Start time: 2024-04-10 13:30:12.747174

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word or phrase) is in the first input (expression), return true, else false, and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function
def generated_function(expression, word):
    # Check if the word is in the expression
    if word in expression:
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

# End time: 2024-04-10 13:30:15.013324
# Elapsed time in seconds: 2.266100827999935


# APPEND TEST SCRIPTS...
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true


print(generated_function("A banana a day keeps the doctor away.", "orange"))  ### Output: [
print(generated_function("Better the devil you know", "devil"))  ### Output: f
print(generated_function("A banana a day keeps the doctor away.", "banana"))  ### Output: a
print(generated_function("A banana a day keeps the doctor away.", "doctor"))  ### Output: l

# TEST SCRIPTS APPENDED!

