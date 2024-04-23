# Start time: 2024-04-09 20:08:45.262882

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing strings that represent names in a "last name,first name" format. Each entry is a combination of a person's last name followed by a comma and then their first name. The names are diverse, covering a range of common first and last names without any apparent restriction on nationality or ethnicity. The data is qualitative, focusing on the categorical nature of personal names. The format is consistent across all entries, adhering to the structure that places the last name before the first name, separated by a comma.

### Output Column Summary:

The output data transforms the format of the names from the input column into a "first name,last name" format. Each entry in the output column is a rearrangement of the corresponding entry in the input column, where the first name is now placed before the last name, separated by a comma. This transformation maintains the integrity of the names while altering their presentation order. The output, like the input, is qualitative and consists of personal names, now presented in a format that is more commonly used in informal and some formal contexts.

### Relationship Summary:

The relationship between the input and output columns is a systematic reordering of the components of personal names. The process involves taking the last name-first name format from the input and flipping it to a first name-last name format in the output. This transformation does not alter the names themselves but changes how they are presented. The operation is consistent across the dataset, applying the same transformation rule to each entry without exception. This reordering facilitates a different way of presenting personal names, potentially making the data more accessible or appropriate for contexts where the first name-last name format is preferred. The transformation highlights the flexibility of data presentation and the importance of format in data interpretation and usage., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    This function takes a name in the format "last name,first name" and
    transforms it into the format "first name,last name".
    
    :param name: A string representing a name in the format "last name,first name".
    :return: A string representing the name in the format "first name,last name".
    """
    # Split the input string into two parts based on the comma
    last_name, first_name = name.split(',')
    # Reorder and combine the names into the desired format
    return f"{first_name},{last_name}"

# Test cases
print(generated_function('chang,amy'))  # Expected output: amy,chang
print(generated_function('smith,bobby'))  # Expected output: bobby,smith
print(generated_function('lennox,aaron'))  # Expected output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-09 20:08:52.956818
# Elapsed time in seconds: 7.693763258997933


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!

