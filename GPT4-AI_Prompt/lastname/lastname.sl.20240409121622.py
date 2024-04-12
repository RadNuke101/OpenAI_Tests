# Start time: 2024-04-09 13:28:47.380759

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in this column is a string that combines the first name and the last name of a person, separated by a space. The dataset includes a variety of names, suggesting a diverse set of individuals. The first names vary widely, indicating no specific pattern or preference towards any particular culture or ethnicity. The last names also show diversity, but each carries a unique identifier for the individual. The structure of the data is consistent across all entries, with each full name following the format of "FirstName LastName".

### Output Column Summary:

The output data consists of a single column that extracts and presents the last name from each full name provided in the input column. This column isolates the second part of each full name, effectively removing the first name and presenting a clear, concise identifier for each individual. The output retains the diversity and uniqueness of the last names found in the input data, focusing solely on this component of the individual's identity. The transformation from input to output demonstrates a consistent method of data simplification and extraction, aimed at isolating a specific piece of information from a more complex dataset.

### Relationship Between Input and Output:

The relationship between the input and output data is characterized by a process of extraction and simplification. The input data provides a more comprehensive view of each individual's identity by including both first and last names. In contrast, the output data distills this information down to only the last name, removing the first name from consideration. This process highlights the last name as a key identifier for each person, while also simplifying the dataset for applications where only this piece of information is necessary. The transformation from input to output demonstrates a clear, systematic approach to isolating a specific component of the data, which could be useful in contexts where the focus is on family names, lineage, or other analyses that prioritize last names over full names., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a full name string.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts and return the last part (last name)
    return full_name.split(" ")[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 13:28:55.891207
# Elapsed time in seconds: 8.510203965999608