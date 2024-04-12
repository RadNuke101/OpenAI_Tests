# Start time: 2024-04-09 20:13:37.921088

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: To summarize the relationship between the input and output data based on the examples provided:

### Input Data Summary:
- The input data consists of strings formatted as three groups of three digits each, separated by hyphens (e.g., "938-242-504").
- Each group within the input data appears to be independent of the others in terms of its relationship to the output.
- The input data is qualitative in nature, with the format and structure being consistent across all examples.

### Output Data Summary:
- The output data consists of three-digit numbers or strings (e.g., "504").
- These outputs are directly extracted from the input data, specifically from the last group of digits in the input string.

### Relationship Summary:
- The relationship between the input and output data is straightforward: the output is always the last group of three digits from the input string.
- There is no transformation or manipulation of the numbers themselves; the output is a direct subset of the input.
- This relationship suggests that the input data's primary function is to carry the output data within a larger string, possibly for formatting or contextual purposes.

In essence, the process to obtain the output from the input involves isolating the last segment of the input string after the second hyphen. This relationship is consistent across all examples provided., and input as ['938-242-504'] output is 504, input as ['308-916-545'] output is 545, input as ['623-599-749'] output is 749, input as ['981-424-843'] output is 843, input as ['118-980-214'] output is 214, input as ['244-655-094'] output is 094, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    """
    Extracts the last group of three digits from the input string.
    
    Parameters:
    input_string (str): A string formatted as three groups of three digits each, separated by hyphens.
    
    Returns:
    str: The last group of three digits from the input string.
    """
    # Split the input string by hyphens and return the last element
    return input_string.split('-')[-1]

# Test cases
print(generated_function('938-242-504'))  # Expected output: 504
print(generated_function('308-916-545'))  # Expected output: 545
print(generated_function('623-599-749'))  # Expected output: 749
print(generated_function('981-424-843'))  # Expected output: 843
print(generated_function('118-980-214'))  # Expected output: 214
print(generated_function('244-655-094'))  # Expected output: 094
print(generated_function("938-242-504"))  ## Output: 504
print(generated_function("308-916-545"))  ## Output: 545
print(generated_function("623-599-749"))  ## Output: 749
print(generated_function("981-424-843"))  ## Output: 843
print(generated_function("118-980-214"))  ## Output: 214
print(generated_function("244-655-094"))  ## Output: 094

# End time: 2024-04-09 20:13:45.401354
# Elapsed time in seconds: 7.480096776998835