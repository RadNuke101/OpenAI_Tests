# Start time: 2024-04-10 13:32:51.000357

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if a number is present in the inputted expression, return true, else false, and input as ['A bird in the hand is worth 2 in the bush.'] output is true, input as ['A bird in the hand is worth two in the bush.'] output is false, input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Check if a number is present in the inputted expression
    if any(char.isdigit() for char in input_str):
        return True
    else:
        return False

# Test cases
generated_function('A bird in the hand is worth 2 in the bush.')
generated_function('A bird in the hand is worth two in the bush.')
generated_function('The 15 shortcuts you simply must know')
print(generated_function("A bird in the hand is worth 2 in the bush."))  ## Output: true
print(generated_function("A bird in the hand is worth two in the bush."))  ## Output: false
print(generated_function("The 15 shortcuts you simply must know"))  ## Output: true

# End time: 2024-04-10 13:32:52.483761
# Elapsed time in seconds: 1.4833735649999653


# APPEND TEST SCRIPTS...
print(generated_function("A bird in the hand is worth 2 in the bush."))  ## Output: true
print(generated_function("A bird in the hand is worth two in the bush."))  ## Output: false
print(generated_function("The 15 shortcuts you simply must know"))  ## Output: true


print(generated_function("You are the first one."))  ### Output: [
print(generated_function("a + b + c + d"))  ### Output: f
print(generated_function("You are the 5st one."))  ### Output: a
print(generated_function("a + b + c + 3"))  ### Output: l
print(generated_function("a + b + c + 1"))  ### Output: s
print(generated_function("You are the 1st one."))  ### Output: e
print(generated_function("You are the 3st one."))  ### Output: ,
print(generated_function("a + b + c + 5"))  ### Output:  

# TEST SCRIPTS APPENDED!

