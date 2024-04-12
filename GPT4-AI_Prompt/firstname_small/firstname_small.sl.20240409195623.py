# Start time: 2024-04-09 20:40:21.829577

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two main parts: the first name and the last name, separated by a space. The dataset includes a diverse set of names, suggesting a variety of cultural backgrounds. Each entry is unique, indicating that the data might represent a sample of individuals from a broader population. The names are presented in a standard format, with the first name followed by the last name, which is a common convention in many cultures. The data is qualitative, focusing on personal identifiers rather than numerical values.

### Output Column Summary:

The output column contains only the first names extracted from the full names provided in the input column. Each output is a single string representing the first name of the individual. This column simplifies the information from the input by isolating a specific component of the data—the first name—thereby reducing the complexity of the information. The output retains the diversity of the input in terms of the variety of names, reflecting the same cultural breadth. Like the input, the output data is qualitative, focusing on the aspect of personal identification through first names.

### Relationship Between Input and Output:

The relationship between the input and output columns is a process of extraction and simplification. The output is derived directly from the input by isolating the first name from the full name provided. This process involves identifying the first space character in the input string and extracting the substring that precedes it, which corresponds to the first name. The transformation from input to output simplifies the data by focusing solely on the first names, removing the last names from consideration. This relationship highlights a method of data reduction, where a specific, consistent piece of information (the first name) is extracted from a more complex dataset (full names). The purpose of this transformation could be to facilitate analyses or applications where only the individual's first name is relevant, thereby streamlining the dataset for specific uses., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the first name from a full name string.

    Parameters:
    full_name (str): A string containing the full name of an individual.

    Returns:
    str: The first name extracted from the full name.
    """
    # Split the full name by space and return the first element
    return full_name.split(' ')[0]

# Test cases
generated_function('Nancy FreeHafer')  # Expected output: 'Nancy'
generated_function('Andrew Cencici')  # Expected output: 'Andrew'
generated_function('Jan Kotas')  # Expected output: 'Jan'
generated_function('Mariya Sergienko')  # Expected output: 'Mariya'
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-09 20:40:28.792336
# Elapsed time in seconds: 6.96258194499751