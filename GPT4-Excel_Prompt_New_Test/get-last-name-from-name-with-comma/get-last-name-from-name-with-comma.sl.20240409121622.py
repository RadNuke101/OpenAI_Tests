# Start time: 2024-04-09 12:31:07.656389

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of strings that represent names in a "last name, first name" format. Each entry is a combination of a last name and a first name, separated by a comma. The data is qualitative, focusing on personal names without any inherent numerical value. The names vary in terms of cultural background, indicating a diverse dataset. The last names come first, followed by the first names, suggesting a formal or official listing format often used in directories, official documents, or academic citations.

### Output Column Summary:

The output column consists of strings that represent names in a "first name, last name" format. This transformation indicates a reordering of the elements from the input data, where the first name is now placed before the last name, separated by a comma. The data remains qualitative, maintaining its focus on personal names. The transformation suggests a shift to a more casual or conversational naming format, which is commonly used in social settings, informal documents, or when addressing individuals directly.

### Relationship Summary:

The relationship between the input and output columns is characterized by a systematic transformation of the format in which personal names are presented. Specifically, the transformation involves reversing the order of the first and last names and maintaining the comma as a separator. This shift from a "last name, first name" format to a "first name, last name" format indicates a move from a formal or official naming convention to a more informal or conversational one. The data itself remains unchanged in terms of the actual names; only the presentation order is altered. This transformation can be useful in contexts where the mode of address needs to be adjusted to fit the social or cultural norms of the intended audience or document format., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    This function takes a name in the format "last name, first name" and
    transforms it into the format "first name, last name".
    
    :param name: A string representing a name in the format "last name, first name".
    :return: A string representing the name in the format "first name, last name".
    """
    # Split the input string into first name and last name based on the comma
    last_name, first_name = name.split(',')
    # Strip any leading or trailing spaces from the names
    first_name = first_name.strip()
    last_name = last_name.strip()
    # Return the transformed name
    return f"{first_name} {last_name}"

# Test cases
print(generated_function('chang,amy'))  # Expected output: amy chang
print(generated_function('smith,bobby'))  # Expected output: bobby smith
print(generated_function('lennox,aaron'))  # Expected output: aaron lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-09 12:31:17.556891
# Elapsed time in seconds: 9.900299066000002


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!

