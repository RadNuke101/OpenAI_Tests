# Start time: 2024-04-09 18:17:52.489941

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains names in a "LastName,FirstName" format, where each entry is a string combining a person's last name, a comma, and their first name. This format suggests that the data pertains to individuals, with their names being split into two parts but presented as a single string. The names appear to be of a diverse nature, indicating no specific cultural, geographical, or professional focus within the dataset.

The second column is numerical, containing the digits '1' or '2'. This column does not directly convey any clear meaning without context but is indicative of a categorical or binary choice related to the first column's data. The simplicity of the data in this column suggests it is used to select or indicate a preference between two options.

### Output Column Summary:

The output data is a single column that contains either the first name or the last name of the individuals from the first input column. The output is determined by the value in the second input column: when the value is '1', the output is the individual's first name; when the value is '2', the output is the individual's last name. This indicates that the output is directly derived from the input data, with the second column acting as a selector between the two parts of the name in the first column.

### Relationship Summary:

The relationship between the input and output columns is a function of selection based on the second input column's value. The first input column provides a composite data point (a full name), and the second input column specifies which part of this composite data point should be extracted and presented as the output. Specifically:

- When the second column's value is '1', the function extracts and outputs the first name from the first column.
- When the second column's value is '2', the function extracts and outputs the last name from the first column.

This relationship demonstrates a straightforward, rule-based processing of qualitative data, where the output is contingent upon a simple conditional operation applied to the input data. The process effectively separates composite information into its constituent parts based on a specified criterion, showcasing a basic but essential data manipulation technique., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name, choice):
    """
    Extracts either the first name or the last name from a full name based on a given choice.

    Parameters:
    - full_name (str): The full name in the format "LastName,FirstName".
    - choice (str): A string representing the choice ('1' for first name, '2' for last name).

    Returns:
    - str: The selected part of the name based on the choice.
    """
    # Split the full name by the comma to separate the last name and the first name
    name_parts = full_name.split(',')
    # Convert the choice to an integer for indexing
    choice_index = int(choice) - 1  # Subtract 1 to convert to 0-based index

    # Return the selected part of the name
    return name_parts[choice_index]

# Test cases
print(generated_function('Chang,Amy', '1'))  # Expected output: Amy
print(generated_function('Chang,Amy', '2'))  # Expected output: Chang
print(generated_function('smith,bobby', '2'))  # Expected output: smith
print(generated_function('smith,bobby', '1'))  # Expected output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-09 18:18:01.711120
# Elapsed time in seconds: 9.220953230000305


# APPEND TEST SCRIPTS...
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby


print(generated_function("parker,olivia", "1"))  ### Output: olivia
print(generated_function("parker,olivia", "2"))  ### Output: parker
print(generated_function("Turner,Jackson", "2"))  ### Output: Turner
print(generated_function("Turner,Jackson", "1"))  ### Output: Jackson

# TEST SCRIPTS APPENDED!

