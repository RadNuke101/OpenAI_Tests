# Start time: 2024-04-05 16:33:31.226647

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
        # If the target word is not found in either phrase, return an empty string
        return ""

# Test cases
print(generated_function('I love apples', 'I hate bananas', 'banana'))  # Expected output: 'I hate bananas'
print(generated_function('I love apples', 'I hate bananas', 'apple'))   # Expected output: 'I love apples'
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples

# End time: 2024-04-05 16:33:35.175557
# Elapsed time in seconds: 3.948855529999946


# APPEND TEST SCRIPTS...
print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples


print(generated_function("I like bananas", "I dislike apples", "apple"))  ### Output: I dislike apples
print(generated_function("I like bananas", "I dislike apples", "banana"))  ### Output: I like bananas

# TEST SCRIPTS APPENDED!

