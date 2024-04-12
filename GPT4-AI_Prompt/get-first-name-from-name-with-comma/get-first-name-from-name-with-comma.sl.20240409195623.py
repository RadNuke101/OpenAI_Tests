# Start time: 2024-04-09 20:02:32.535316

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains names in a "LastName,FirstName" format, representing individuals' names with their last names followed by a comma and then their first names. This format suggests a structured approach to capturing names, emphasizing the distinction between last and first names by separating them with a comma. The names appear to be of a personal nature, likely representing individuals' real names or possibly fictional characters, but consistently maintaining the "LastName,FirstName" structure.

The second column contains numerical values, specifically '1' or '2'. These numbers are qualitative indicators rather than quantitative values, as they do not measure or count anything directly but instead signify a choice or an option. The presence of only two options suggests a binary classification or selection mechanism within the context of the input data.

### Output Column Summary:

The output data is a single column that contains names, either a first name or a last name, depending on the corresponding numerical value in the second input column. When the numerical value is '1', the output is the first name of the individual. Conversely, when the numerical value is '2', the output is the last name. This indicates a direct relationship between the second input column and the format of the output, where the numerical value acts as a selector between the first and last names provided in the first input column.

### Relationship Summary:

The relationship between the input and the output data is governed by the numerical value in the second input column, which serves as a key to selecting either the first or last name from the first input column. This selection mechanism is consistent across all data points, demonstrating a clear, rule-based relationship. The process transforms a structured full name into either its component first or last name based on the binary choice represented by '1' or '2'. This transformation suggests a filtering or parsing operation that extracts specific elements from a composite string based on a given criterion.

In summary, the input data combines structured name information with a binary selector to produce an output that is either the first or last name from the input. This demonstrates a straightforward, rule-based method for parsing and selectively extracting information from a composite data format., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name, selector):
    """
    Extracts either the first name or the last name from a full name based on the selector value.
    
    Parameters:
    - full_name (str): The full name in "LastName,FirstName" format.
    - selector (str): A string representing the selector value ('1' for first name, '2' for last name).
    
    Returns:
    - str: The selected name part (either first name or last name).
    """
    # Split the full name by the comma to separate the last name and the first name
    name_parts = full_name.split(',')
    # Convert the selector to an integer for indexing
    selector_index = int(selector) - 1  # Subtract 1 to match list indexing (0-based)
    
    # Return the selected name part based on the selector value
    return name_parts[selector_index]

# Test cases
# Test case 1: Selector '1', expecting first name 'Amy'
print(generated_function('Chang,Amy', '1'))  # Output: Amy

# Test case 2: Selector '2', expecting last name 'Chang'
print(generated_function('Chang,Amy', '2'))  # Output: Chang

# Test case 3: Selector '2', expecting last name 'smith' (lowercase intentional)
print(generated_function('smith,bobby', '2'))  # Output: smith

# Test case 4: Selector '1', expecting first name 'bobby' (lowercase intentional)
print(generated_function('smith,bobby', '1'))  # Output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-09 20:02:45.989680
# Elapsed time in seconds: 13.454061839998758