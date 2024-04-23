# Start time: 2024-04-09 16:36:28.863198

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains names in a "LastName,FirstName" format, representing individuals' names. These names are structured such that the last name and first name are separated by a comma, with the last name appearing first. The names provided are diverse, including both common and potentially less common surnames and given names, indicating a variety of individuals. The capitalization is consistent, with the first letter of each name capitalized, suggesting a standard naming convention.

The second column is numerical, containing the digits '1' or '2'. This column appears to serve as an indicator or selector, potentially instructing how to interpret or manipulate the data in the first column.

### Output Column Summary:

The output data is a single column that contains names, either a first name or a last name, depending on the indicator provided in the second input column. When the indicator is '1', the output is the first name of the individual. Conversely, when the indicator is '2', the output is the last name. This suggests that the output is directly derived from the first input column, with the second input column acting as a key to select which part of the name to output.

### Relationship Summary:

The relationship between the input and output columns is a function of selection based on the indicator provided in the second input column. The process can be summarized as follows:

1. **Name Parsing**: The first input column provides a full name in a "LastName,FirstName" format. This format is consistent across all entries, allowing for a predictable parsing of the names into their constituent parts.

2. **Indicator Function**: The second input column serves as an indicator or selector. The value within this column ('1' or '2') determines which part of the name from the first column is selected for output:
   - A value of '1' indicates that the first name (post-comma segment) should be selected.
   - A value of '2' indicates that the last name (pre-comma segment) should be selected.

3. **Output Generation**: Based on the indicator, the corresponding part of the name is extracted and presented as the output. This output is singular, focusing on either the first name or the last name, but not both.

This relationship showcases a straightforward, rule-based selection process, where the input directly influences the output through a defined indicator. The system is qualitative, focusing on the manipulation of text data (names) rather than performing any quantitative analysis., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name, indicator):
    """
    Extracts and returns either the first name or the last name from a full name based on the indicator.
    
    Parameters:
    - full_name (str): The full name in "LastName,FirstName" format.
    - indicator (str): A string that is either '1' or '2', where '1' indicates selecting the first name and '2' indicates selecting the last name.
    
    Returns:
    - str: The selected part of the name based on the indicator.
    """
    # Split the full name into last name and first name based on the comma
    parts = full_name.split(',')
    last_name = parts[0]
    first_name = parts[1]
    
    # Return the appropriate part of the name based on the indicator
    if indicator == '1':
        return first_name
    elif indicator == '2':
        return last_name
    else:
        return "Invalid indicator"

# Test cases
# Note: The actual test execution and output verification are not included as per the instructions.

# Test case 1
# Input: ['Chang,Amy', '1']
# Expected Output: 'Amy'

# Test case 2
# Input: ['Chang,Amy', '2']
# Expected Output: 'Chang'

# Test case 3
# Input: ['smith,bobby', '2']
# Expected Output: 'smith'

# Test case 4
# Input: ['smith,bobby', '1']
# Expected Output: 'bobby'
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-09 16:36:41.325729
# Elapsed time in seconds: 12.462391503000617


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

