# Start time: 2024-04-09 16:41:25.119237

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column, where each entry is a string formatted as 'lastname,firstname'. The entries are composed of two parts: the first part represents the last name of an individual, and the second part represents the first name. These parts are separated by a comma. The data appears to represent names of individuals, with their surnames appearing first followed by their given names. The names are in a mixed case, suggesting no specific case format is enforced. The dataset includes a variety of names, indicating a diverse set of entries without any apparent restriction on name origin or structure.

### Output Column Summary:

The output data, corresponding to the input, is also formatted as strings but with the order of the names reversed to 'firstname,lastname'. This transformation suggests that the process involves swapping the positions of the first and last names and maintaining the original case of each part. The output retains the comma as a separator between the first and last names. The output dataset mirrors the diversity and structure of the input dataset, with the key difference being the order in which the names are presented.

### Relationship Summary:

The relationship between the input and output data columns is a systematic transformation of the format in which individual names are presented. Specifically, the process involves reversing the order of the first and last names from the input to the output. This transformation does not alter the case of the names or introduce any additional characters beyond swapping the positions of the names around the comma separator. The process is consistent across all entries, indicating a rule-based approach to reformatting the names. This transformation could be useful in contexts where the preferred or required format for presenting names is 'firstname,lastname' rather than 'lastname,firstname'. The relationship showcases a straightforward, predictable mapping from the input format to the output format, facilitating easy understanding and potential automation of the process for large datasets., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    This function takes a string input in the format 'lastname,firstname'
    and returns a string in the format 'firstname,lastname'.
    """
    # Split the input string into two parts based on the comma separator
    parts = name.split(',')
    # Reverse the order of the parts and join them back with a comma
    reversed_name = parts[1] + ',' + parts[0]
    return reversed_name

# Test cases
print(generated_function('chang,amy'))  # Expected output: amy,chang
print(generated_function('smith,bobby'))  # Expected output: bobby,smith
print(generated_function('lennox,aaron'))  # Expected output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-09 16:41:31.531389
# Elapsed time in seconds: 6.412079755000377