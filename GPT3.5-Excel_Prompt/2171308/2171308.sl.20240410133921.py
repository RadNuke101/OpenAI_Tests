# Start time: 2024-04-10 13:44:22.412875

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into two words
    words = input_str.split()
    
    # Extract the first letter of the first word and the second word
    first_letter = words[0][0]
    second_word = words[1]
    
    # Return the formatted output
    return first_letter + ' ' + second_word

# Test cases
print(generated_function('John Doe'))
print(generated_function('Mayur Naik'))
print(generated_function('Nimit Singh'))
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 13:44:24.458197
# Elapsed time in seconds: 2.045275280000169