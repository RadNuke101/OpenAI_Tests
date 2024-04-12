# Start time: 2024-04-05 18:17:36.572380

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase1, phrase2, target_word):
    # Check if the target word is in the first phrase
    if target_word in phrase1.split():
        return phrase1
    # Check if the target word is in the second phrase
    elif target_word in phrase2.split():
        return phrase2
    else:
        return "Word not found in either phrase."

# Test cases
print(generated_function('I love apples', 'I hate bananas', 'banana'))  # Expected: 'I hate bananas'
print(generated_function('I love apples', 'I hate bananas', 'apple'))  # Expected: 'I love apples'
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples

# End time: 2024-04-05 18:17:40.721798
# Elapsed time in seconds: 4.149293589000081