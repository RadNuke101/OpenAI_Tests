# Start time: 2024-04-09 17:01:38.312220

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, which are structured in a variety of formats. These names are composed of first names, middle initials or names, and last names. The dataset includes names from diverse cultural backgrounds, as indicated by the variety of name structures and origins, such as "Susan Ann Chang" and "Ayako Tanaka". The presence of middle initials, as seen in "Bobby T. smth", suggests a mix of formal and informal naming conventions. The input data is qualitative, focusing on the unique identification of individuals through their names.

### Output Column Summary:

The output column extracts and presents the first name from each full name provided in the input column. Regardless of the cultural background, naming convention, or the complexity of the full name, the output consistently isolates the first given name of the individual. This process simplifies the identification of individuals by their first name, facilitating a more straightforward way to address or refer to them in contexts where the full name is unnecessary or too formal.

### Relationship Between Input and Output:

The relationship between the input and output columns is characterized by a systematic extraction process, where the output is derived by isolating the first given name from the full name provided in the input. This transformation demonstrates a focus on simplification and the prioritization of first names as primary identifiers in social or formal contexts. The process respects the diversity of naming conventions across different cultures by uniformly applying the extraction rule to all entries, ensuring consistency in the output. The transformation from full names to first names highlights the importance of first names in personal identification and interaction, while also acknowledging the complexity and richness of cultural naming practices captured in the input data., and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the first name from a given full name.

    Parameters:
    full_name (str): The full name of an individual.

    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name by spaces to isolate the first name
    name_parts = full_name.split()
    # Return the first part, which is the first name
    return name_parts[0]

# Test cases
first_name1 = generated_function('Susan Ann Chang')
first_name2 = generated_function('Ayako Tanaka')
first_name3 = generated_function('Bobby T. smth')
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-09 17:01:45.686473
# Elapsed time in seconds: 7.374108315001649