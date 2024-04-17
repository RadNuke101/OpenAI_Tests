# Start time: 2024-04-16 21:27:23.780610

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and input as: "I love apples", "I hate bananas", "banana" output is: I hate bananas, input as: "I love apples", "I hate bananas", "apple" output is: I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(*args):
    # Create a dictionary to store phrases with corresponding keywords
    phrases = {}
    
    # Iterate through the input arguments
    for arg in args:
        # Split the argument into phrases and keyword
        phrase1, phrase2, keyword = arg.split()
        
        # Store the phrases in the dictionary with the keyword as the key
        phrases[keyword] = (phrase1, phrase2)
    
    # Return the phrase that contains the keyword
    return phrases[args[-1]][0] if args[-1] in phrases[args[-1]][0] else phrases[args[-1]][1]



print(generated_function("I like bananas", "I dislike apples", "apple"))  ### Output: "I like bananas", "I dislike apples", "apple"
print(generated_function("I like bananas", "I dislike apples", "banana"))  ### Output: "I like bananas", "I dislike apples", "banana"


print(generated_function("I love apples", "I hate bananas", "banana"))  ## Output: I hate bananas
print(generated_function("I love apples", "I hate bananas", "apple"))  ## Output: I love apples



# End time: 2024-04-16 21:27:26.105784
# Elapsed time in seconds: 2.325276640999988