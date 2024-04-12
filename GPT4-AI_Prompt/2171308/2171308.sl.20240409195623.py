# Start time: 2024-04-09 20:39:33.080114

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of full names of individuals, each entry formatted as a single string. These names are structured in a conventional Western naming format, where each entry typically includes a given name followed by a surname. The given names and surnames are diverse, indicating a variety of cultural backgrounds. Each entry is unique, suggesting a dataset of distinct individuals. The data is qualitative, focusing on the textual representation of names rather than any numerical attribute.

### Summary of Output Column Data

The output data transforms the input full names into a more abbreviated format. Each output entry retains the initial of the given name followed by the full surname, formatted as a single string. This transformation results in a consistent, concise representation of the original names, emphasizing the surname while still providing a hint of the given name through its initial. The output maintains the diversity and uniqueness of the input data, albeit in a more compact form.

### Relationship Between Input and Output

The transformation from input to output data demonstrates a systematic reduction of the qualitative information from a full name to an abbreviated version. This process involves extracting the initial from the given name and preserving the surname in its entirety. The relationship between the input and output data is characterized by a consistent rule applied across all entries, aimed at simplifying the representation of names while retaining enough information to maintain distinctiveness and a degree of personal identity. This transformation could serve purposes such as creating usernames, generating initials for monograms, or any context where space or simplicity is a priority. The method preserves the cultural diversity present in the surnames and ensures that each transformed name remains linked to its original form, facilitating recognition and association between the abbreviated and full names., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Transforms a full name into an abbreviated format where the given name is reduced to its initial
    and the surname is retained in full.

    Parameters:
    full_name (str): The full name of an individual, formatted as 'GivenName Surname'.

    Returns:
    str: The abbreviated name, formatted as 'Initial Surname'.
    """
    # Split the full name into given name and surname
    parts = full_name.split()
    # Extract the initial of the given name and the full surname
    abbreviated_name = parts[0][0] + " " + parts[1]
    return abbreviated_name

# Test cases
print(generated_function('John Doe'))  # Expected output: J Doe
print(generated_function('Mayur Naik'))  # Expected output: M Naik
print(generated_function('Nimit Singh'))  # Expected output: N Singh
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-09 20:39:40.044448
# Elapsed time in seconds: 6.964153528999304