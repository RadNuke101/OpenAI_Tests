# Start time: 2024-04-05 17:42:35.834405

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase1, phrase2, target_word):
    # Check if the target word is in the first phrase
    if target_word.lower() in phrase1.lower():
        return phrase1
    # Check if the target word is in the second phrase
    elif target_word.lower() in phrase2.lower():
        return phrase2
    else:
        return "The word is not found in either phrase."

# Test cases
result1 = generated_function('I love apples', 'I hate bananas', 'banana')
result2 = generated_function('I love apples', 'I hate bananas', 'apple')

# The function will return the phrase containing the target word
# The outputs can be checked by printing result1 and result2
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples

# End time: 2024-04-05 17:42:40.181745
# Elapsed time in seconds: 4.347226036999928