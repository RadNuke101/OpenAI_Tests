# Start time: 2024-04-16 14:25:33.640710

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function to match the given input and output
def generated_function(phrase1, phrase2, word):
    # Check if the word is in the first phrase
    if word in phrase1:
        return phrase1
    # Check if the word is in the second phrase
    elif word in phrase2:
        return phrase2

# Test cases
generated_function('I love apples', 'I hate bananas', 'banana')
generated_function('I love apples', 'I hate bananas', 'apple')



print(generated_function("I like bananas", "I dislike apples", "apple"))  ### Output: "I like bananas", "I dislike apples", "apple"
print(generated_function("I like bananas", "I dislike apples", "banana"))  ### Output: "I like bananas", "I dislike apples", "banana"


print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples



# End time: 2024-04-16 14:25:35.486166
# Elapsed time in seconds: 1.8454078030000005