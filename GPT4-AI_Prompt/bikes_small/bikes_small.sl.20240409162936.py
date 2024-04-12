# Start time: 2024-04-09 17:36:31.827774

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary

The input data consists of strings that are a combination of a brand name followed by a numeric value. The brand names observed in the input data are "Ducati" and "Honda." The numeric values that follow the brand names are 100, 125, 250, and 550. These numeric values seem to represent a model or specification related to the brand, but without further context, it's unclear what these numbers specifically denote (e.g., engine capacity, model number). The input data format is consistent across all entries, following the pattern of [BrandName][NumericValue] without any spaces.

### Output Column Summary

The output data extracts and presents only the brand name part of the input strings, effectively removing the numeric values that follow the brand names. The output data consists of the brand names "Ducati" and "Honda" exclusively. This indicates that the process or function applied to the input data is designed to isolate and return only the brand name component of each input string.

### Relationship Summary

The relationship between the input and output data is a straightforward extraction operation where the goal is to separate the brand name from the numeric value in the input strings. The process ignores the numeric values and retains only the brand names as the output. This suggests that the operation or function applied is capable of identifying and extracting alphabetical characters that form the brand name up to the point where numeric characters start. The relationship does not account for variations in the numeric values following the brand names, as they do not influence the output. The operation is consistent across different numeric values, indicating that the focus is solely on the brand name component of the input data., and input as ['Ducati100'] output is Ducati, input as ['Honda125'] output is Honda, input as ['Ducati250'] output is Ducati, input as ['Honda250'] output is Honda, input as ['Honda550'] output is Honda, input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Extract the brand name from the input string by removing numeric values
    brand_name = ''.join(filter(lambda x: not x.isdigit(), input_string))
    return brand_name

# Test cases based on the provided input and output
print(generated_function('Ducati100'))  # Expected output: Ducati
print(generated_function('Honda125'))   # Expected output: Honda
print(generated_function('Ducati250'))  # Expected output: Ducati
print(generated_function('Honda250'))   # Expected output: Honda
print(generated_function('Honda550'))   # Expected output: Honda
print(generated_function('Ducati125'))  # Expected output: Ducati
print(generated_function("Ducati100"))  ## Output: Ducati
print(generated_function("Honda125"))  ## Output: Honda
print(generated_function("Ducati250"))  ## Output: Ducati
print(generated_function("Honda250"))  ## Output: Honda
print(generated_function("Honda550"))  ## Output: Honda
print(generated_function("Ducati125"))  ## Output: Ducati

# End time: 2024-04-09 17:36:37.051982
# Elapsed time in seconds: 5.224063901998306