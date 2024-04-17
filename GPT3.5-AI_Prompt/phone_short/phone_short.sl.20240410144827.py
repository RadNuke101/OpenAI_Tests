# Start time: 2024-04-10 14:48:34.093332

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers in the format XXX-XXX-XXX. Each phone number is unique and does not repeat in the dataset. The numbers in the input column data do not follow any specific pattern or sequence.

Summary for Output Column:
The output column consists of the first set of numbers from each phone number in the input column data. These numbers range from 118 to 981 and do not follow any specific pattern or sequence. Each output number corresponds to a unique input phone number.

Relationship between Input and Output:
The output number is the first set of numbers from each phone number in the input column data. There is no apparent relationship or pattern between the input phone numbers and the output numbers. Each input phone number corresponds to a unique output number, with no repetition or specific order. The output number seems to be randomly selected from the input phone numbers without any discernible connection., and input as ['938-242-504'] output is 938, input as ['308-916-545'] output is 308, input as ['623-599-749'] output is 623, input as ['981-424-843'] output is 981, input as ['118-980-214'] output is 118, input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Extract the first set of numbers from the input phone number
    output = input_str.split('-')[0]
    
    return output

# Test cases
generated_function('938-242-504')
generated_function('308-916-545')
generated_function('623-599-749')
generated_function('981-424-843')
generated_function('118-980-214')
generated_function('244-655-094')
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244

# End time: 2024-04-10 14:48:35.721516
# Elapsed time in seconds: 1.6281390679998822