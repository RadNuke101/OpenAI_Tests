# Start time: 2024-04-10 14:24:15.767925

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: For the input column data, each entry consists of a three-digit number followed by two hyphens and another three-digit number. The first three-digit number in each entry represents a unique identifier or code. The second three-digit number seems to be random and does not follow a specific pattern. 

As for the output column, it consists of the first three-digit number from each input entry. This number serves as a key or reference point for each input data. The output column essentially extracts and highlights the unique identifier from the input data.

Therefore, the relationship between the input and output columns is that the output column is derived from the first three-digit number in each input entry. The output column acts as a summarized version of the input data, focusing on the key identifier present in each entry., and input as ['938-242-504'] output is 938, input as ['308-916-545'] output is 308, input as ['623-599-749'] output is 623, input as ['981-424-843'] output is 981, input as ['118-980-214'] output is 118, input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for arg in args:
        output.append(int(arg.split('-')[0]))
    return output

# Test cases
generated_function('938-242-504', '308-916-545', '623-599-749', '981-424-843', '118-980-214', '244-655-094')
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244

# End time: 2024-04-10 14:24:17.060879
# Elapsed time in seconds: 1.2929299490000012


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244


print(generated_function("234-424-843"))  ### Output: 234
print(generated_function("789-599-749"))  ### Output: 789
print(generated_function("345-980-214"))  ### Output: 345
print(generated_function("123-242-504"))  ### Output: 123
print(generated_function("456-916-545"))  ### Output: 456
print(generated_function("678-655-094"))  ### Output: 678

# TEST SCRIPTS APPENDED!

