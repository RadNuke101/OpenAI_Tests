# Start time: 2024-04-10 18:18:50.634724

'''
Prompt:
Given that input as ['india china japan'] output is india china, input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string into a list of words
        words = input_str.split()
        
        # Check if the input contains more than one word
        if len(words) > 1:
            # Return the first two words joined by a space
            return ' '.join(words[:2])
        else:
            # Return the single word
            return words[0]
    
    except Exception as e:
        # Handle any exceptions that may occur
        return "Error: Invalid input"

# Test cases
print(generated_function('india china japan'))
print(generated_function('indonesia korea'))
print(generated_function("india china japan"))  ## Output: india china
print(generated_function("indonesia korea"))  ## Output: indonesia

# End time: 2024-04-10 18:18:52.619117
# Elapsed time in seconds: 1.9843479789997218


# APPEND TEST SCRIPTS...
print(generated_function("india china japan"))  ## Output: india china
print(generated_function("indonesia korea"))  ## Output: indonesia


print(generated_function("china india japan"))  ### Output: india china
print(generated_function("korea indonesia"))  ### Output: indonesia
print(generated_function("argentina korea india"))  ### Output: argentina india
print(generated_function("finland india"))  ### Output: finland india

# TEST SCRIPTS APPENDED!

