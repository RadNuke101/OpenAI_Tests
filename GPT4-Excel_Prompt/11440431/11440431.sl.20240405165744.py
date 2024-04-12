# Start time: 2024-04-05 17:19:58.287680

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the last phrase / word if all the letters are capitalized, and input as ['Mining US'] output is Mining, input as ['Soybean Farming CAN'] output is Soybean Farming, input as ['Soybean Farming'] output is Soybean Farming, input as ['Oil Extraction US'] output is Oil Extraction, input as ['Fishing'] output is Fishing, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Split the input string into words
    words = input_string.split()
    # Check if the last word is fully capitalized
    if words[-1].isupper():
        # Remove the last word
        return ' '.join(words[:-1])
    else:
        # Return the input string as is if the last word is not fully capitalized
        return input_string

# Test cases
generated_function('Mining US')
generated_function('Soybean Farming CAN')
generated_function('Soybean Farming')
generated_function('Oil Extraction US')
generated_function('Fishing')
print(generated_function("Mining US"))  ## Output: Mining
print(generated_function("Soybean Farming CAN"))  ## Output: Soybean Farming
print(generated_function("Soybean Farming"))  ## Output: Soybean Farming
print(generated_function("Oil Extraction US"))  ## Output: Oil Extraction
print(generated_function("Fishing"))  ## Output: Fishing

# End time: 2024-04-05 17:20:02.479090
# Elapsed time in seconds: 4.191290336999373