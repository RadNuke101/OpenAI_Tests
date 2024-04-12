# Start time: 2024-04-09 15:10:05.742794

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in this column is a string that includes a first name followed by a last name, with both names separated by a space. The names appear to be of diverse origins, indicating a variety of cultural backgrounds. The data does not include any titles, prefixes, or suffixes attached to the names, focusing solely on the personal and family names of the individuals.

### Output Column Summary:

The output data, corresponding to the input data, transforms each full name into a format that includes a professional title followed by the individual's first name. Specifically, each output entry prefixes the title "Dr." to the first name of the individual from the input data, omitting the last name entirely. This transformation standardizes the format across all entries, applying the same professional title to each individual regardless of their original name's cultural background or complexity.

### Relationship Summary:

The relationship between the input and output data demonstrates a process of formalization and simplification of names by applying a professional title and retaining only the first name from the input. This process involves:

1. **Extraction of the First Name:** The transformation extracts the first name from the full name provided in the input data, discarding the last name. This step simplifies the identity to its most basic and personal component—the individual's first name.

2. **Addition of a Professional Title:** Each transformed name is prefixed with the title "Dr.," which introduces a formal and professional context to the name. This addition implies a level of respect or academic/professional achievement, standardizing the way individuals are addressed regardless of their original name's form or cultural background.

3. **Standardization:** The output data presents a uniform format for addressing individuals, which could be useful in contexts where a consistent and formal mode of address is preferred. This transformation does not discriminate based on the complexity or origin of the names, applying the same rule to all entries.

In summary, the transformation from input to output represents a formalization process that simplifies names by focusing on the first name and standardizes the mode of address by applying a professional title. This process could be particularly relevant in environments where a uniform and respectful way of addressing individuals is necessary, such as academic, medical, or professional settings., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Transforms a full name by extracting the first name and prefixing it with 'Dr.'.

    Parameters:
    full_name (str): A string containing the first name and last name separated by a space.

    Returns:
    str: A string with the title 'Dr.' followed by the first name extracted from the input.
    """
    # Split the full name into first name and last name
    first_name = full_name.split(' ')[0]
    # Prefix the first name with 'Dr.' and return
    return f"Dr. {first_name}"

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 15:10:13.857448
# Elapsed time in seconds: 8.114522223000677