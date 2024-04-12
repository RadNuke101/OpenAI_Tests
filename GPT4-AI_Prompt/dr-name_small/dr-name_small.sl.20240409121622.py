# Start time: 2024-04-09 13:48:15.586903

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of a list of full names, each entry containing a first name followed by a last name. These names represent individuals, with a diverse set of origins suggested by the variety in the surnames. The names are structured in a consistent format, with the first name leading, followed by the last name, and each name is a single word without any titles or suffixes. The data is qualitative, representing personal identifiers without implying any hierarchical or numerical value.

### Output Column Summary:

The output column contains a transformation of the input names, where each entry is prefixed with the title "Dr." followed by the first name of the individual from the input column. The last names are omitted in the output, simplifying the identifier to a title and first name only. This transformation uniformly applies a professional or academic honorific to each individual, suggesting a level of respect or qualification without altering the original first names. The output remains qualitative, focusing on personal identification with an added layer of formal recognition.

### Relationship Between Input and Output:

The relationship between the input and output columns is a systematic transformation that applies a uniform modification to each entry. Specifically, the transformation:

1. Retains the first name from each input entry.
2. Omits the last name from each input entry.
3. Prefixes each retained first name with the title "Dr.", indicating a form of professional or academic recognition.

This process suggests a standardization or formalization of the input names, where the essence of personal identity (the first name) is maintained while the context of the name is shifted towards a more formal or professional setting. The relationship underscores a consistent application of a rule across diverse data, demonstrating how qualitative data can be uniformly modified to reflect a specific attribute or status without altering the core identity represented by the first names., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Transforms a given full name by retaining the first name and prefixing it with 'Dr.'.

    Parameters:
    full_name (str): The full name of an individual, consisting of a first name and a last name.

    Returns:
    str: A transformed name with the title 'Dr.' prefixed to the first name.
    """
    # Split the full name into first name and last name
    first_name = full_name.split()[0]
    # Prefix 'Dr.' to the first name
    transformed_name = "Dr. " + first_name
    return transformed_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))   # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))        # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko')) # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 13:48:26.223090
# Elapsed time in seconds: 10.635872814999857