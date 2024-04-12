# Start time: 2024-04-09 18:22:28.255710

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of strings that represent names in a "last name,first name" format. Each entry is a combination of a last name and a first name separated by a comma, with no spaces in between. The data is qualitative, focusing on personal names. The names vary in length and ethnic origin, reflecting a diversity of backgrounds. The format is consistent across all entries, adhering to the "last name,first name" structure.

### Output Column Summary:

The output column consists of strings that represent names in a "first name,last name" format. Each entry is a transformation of the input data, where the first name now precedes the last name, separated by a comma. Unlike the input, the output format emphasizes the individual's first name, making it more personal and direct. The transformation maintains the integrity of the names, ensuring that the spelling and order of the names within each entry are preserved, only altering the position of the first and last names.

### Relationship Summary:

The relationship between the input and output columns is a systematic reformatting of personal names from a "last name,first name" structure to a "first name,last name" structure. This transformation highlights a shift in focus from a formal or official naming convention, often used in lists or administrative contexts, to a more casual or personal format, which might be used in informal settings or where individual identity is emphasized. The process does not alter the names themselves but rearranges the order in which the first and last names are presented. This reformatting can be seen as a way to humanize or personalize the data, making it more accessible or relatable to the reader., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    # Split the input string into first name and last name based on the comma
    last_name, first_name = name.split(',')
    # Reformat the name to "first name,last name"
    reformatted_name = f"{first_name},{last_name}"
    # Return the reformatted name
    return reformatted_name

# Test cases
result1 = generated_function('chang,amy')
result2 = generated_function('smith,bobby')
result3 = generated_function('lennox,aaron')

# The results can be printed or used further in the code
print(result1)  # Expected output: amy,chang
print(result2)  # Expected output: bobby,smith
print(result3)  # Expected output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-09 18:22:34.409880
# Elapsed time in seconds: 6.154020591002336