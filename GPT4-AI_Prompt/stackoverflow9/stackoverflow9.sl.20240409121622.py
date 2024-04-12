# Start time: 2024-04-09 13:55:22.884672

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary

The input column consists of full names of individuals, each presented as a single string within an array. These names follow a common naming convention where each name is composed of multiple parts, typically including a first name, a middle name or names, and a last name. The structure of the names suggests a Western naming convention, where the first part is usually the given name, followed by middle name(s), and ending with the family name or surname. The names are diverse in terms of the number of components they contain, indicating variability in the way individuals' names are represented. Each entry in the input column is unique, reflecting a dataset of distinct individuals.

### Output Column Summary

The output column consists of the last names extracted from the full names provided in the input column. Each output is a single string, representing the surname of the individual named in the corresponding input row. The output strings are concise, containing only the last name without any additional names or titles. This simplification process transforms the detailed personal information from the input into a more focused dataset, emphasizing the family or surname component of each individual's name.

### Relationship Between Input and Output

The relationship between the input and output columns is characterized by a process of extraction and simplification, where the complex, multi-part names in the input are reduced to their essential surname components in the output. This transformation highlights the importance of the surname as a key identifier within the dataset, stripping away the additional context provided by first and middle names. The process suggests an analytical focus on lineage, family connections, or other contexts where the surname is of primary interest. The consistent methodology applied across the dataset ensures that the output column provides a uniform view of the surname information, making it suitable for applications where this level of detail is sufficient. This relationship underscores the utility of processing qualitative data to extract specific, relevant information according to predefined criteria, in this case, isolating the surname from a full name., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a given full name.
    
    Parameters:
    full_name (str): A string representing a full name following a Western naming convention.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.split()
    # The last name is assumed to be the last part of the split full name
    last_name = name_parts[-1]
    return last_name

# Test cases
# Test with the name 'Sarah Jane Jones'
print(generated_function('Sarah Jane Jones'))  # Expected output: Jones

# Test with the name 'Bob Jane Smithfield'
print(generated_function('Bob Jane Smithfield'))  # Expected output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-09 13:55:30.928317
# Elapsed time in seconds: 8.043413417999545