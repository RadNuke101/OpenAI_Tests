# Start time: 2024-04-10 13:06:32.803279

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and input as ['Ducati100'] output is Ducati, input as ['Honda125'] output is Honda, input as ['Ducati250'] output is Ducati, input as ['Honda250'] output is Honda, input as ['Honda550'] output is Honda, input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Return the text before the last 3 numbers in inputted expression
    return input_str[:-3]

# Test cases
print(generated_function('Ducati100'))
print(generated_function('Honda125'))
print(generated_function('Ducati250'))
print(generated_function('Honda250'))
print(generated_function('Honda550'))
print(generated_function('Ducati125'))
print(generated_function("Ducati100"))  ## Output: Ducati
print(generated_function("Honda125"))  ## Output: Honda
print(generated_function("Ducati250"))  ## Output: Ducati
print(generated_function("Honda250"))  ## Output: Honda
print(generated_function("Honda550"))  ## Output: Honda
print(generated_function("Ducati125"))  ## Output: Ducati

# End time: 2024-04-10 13:06:34.402812
# Elapsed time in seconds: 1.5995059209999454


# APPEND TEST SCRIPTS...
print(generated_function("Ducati100"))  ## Output: Ducati
print(generated_function("Honda125"))  ## Output: Honda
print(generated_function("Ducati250"))  ## Output: Ducati
print(generated_function("Honda250"))  ## Output: Honda
print(generated_function("Honda550"))  ## Output: Honda
print(generated_function("Ducati125"))  ## Output: Ducati


print(generated_function("Ford250"))  ### Output: Ford
print(generated_function("Ford125"))  ### Output: Ford
print(generated_function("Toyota125"))  ### Output: Toyota
print(generated_function("Toyota550"))  ### Output: Toyota
print(generated_function("Hyundai125"))  ### Output: Hyundai
print(generated_function("Ford100"))  ### Output: Ford
print(generated_function("Hyundai100"))  ### Output: Hyundai
print(generated_function("Lamborghini250"))  ### Output: Lamborghini
print(generated_function("Toyota250"))  ### Output: Toyota

# TEST SCRIPTS APPENDED!

