# Start time: 2024-04-09 17:42:20.644900

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in the column is a string that includes a first name followed by a last name, with both names separated by a space. The names appear to be of diverse origins, indicating a variety of cultural backgrounds among the individuals listed. The data is qualitative, focusing on personal identifiers without any numerical or quantitative information. The format is consistent across the dataset, with each entry adhering to the "FirstName LastName" structure.

### Output Column Summary:

The output data, corresponding to the input data, transforms each full name into a professional title format, specifically by prefixing each first name with "Dr. ". This transformation retains the first name from each input entry while discarding the last name, and adds a professional honorific. The output is also qualitative, emphasizing a formal or professional recognition of each individual. The consistency in the output format underscores a uniform application of the transformation rule across the diverse set of names.

### Relationship Summary:

The relationship between the input and output data is a systematic transformation that focuses on the formalization and professionalization of personal names. This transformation involves two key steps: (1) extracting the first name from each full name in the input, and (2) prefixing this first name with the title "Dr. " to generate the output. The process discards the last name and does not differentiate based on the origin or cultural background of the name. The transformation suggests a context where the professional title is of primary importance, possibly for a setting where formal recognition or academic achievement is being highlighted. The consistent application of this rule across a diverse set of names indicates an overarching emphasis on professional identity over individual identity as represented by the full name., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Transforms a full name into a professional title format by prefixing the first name with "Dr. " and discarding the last name.

    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.

    Returns:
    str: A string with the first name prefixed by "Dr. ", discarding the last name.
    """
    # Split the full name into first name and last name
    first_name = full_name.split()[0]
    # Prefix the first name with "Dr. " and return the result
    return "Dr. " + first_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 17:42:27.621175
# Elapsed time in seconds: 6.976083025998378