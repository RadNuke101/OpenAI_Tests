# Start time: 2024-04-09 14:35:09.586398

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains names in a "Lastname,Firstname" format, representing individuals' names with their last names followed by a comma and then their first names. This format suggests a structured approach to capturing full names, emphasizing the distinction between last and first names. The second column contains numerical values, either '1' or '2', which appear to serve as indicators or selectors for the output.

### Output Column Summary:

The output data is derived from the input data, specifically from the first column of names. It consists of either the first name or the last name of the individuals, depending on the value provided in the second input column. When the value is '1', the output is the individual's first name. Conversely, when the value is '2', the output is the individual's last name. This suggests a direct relationship between the second column of the input data and the format of the output data.

### Relationship Between Input and Output:

The relationship between the input and output data is governed by the value in the second column of the input data. This value acts as a selector or switch that determines which part of the name (first or last) from the first input column is extracted and presented as the output. Specifically:

- A value of '1' in the second input column corresponds to extracting and outputting the first name from the first input column.
- A value of '2' in the second input column corresponds to extracting and outputting the last name from the first input column.

This mechanism allows for a dynamic extraction of names based on a simple, numerical instruction, showcasing a straightforward yet effective method of data manipulation and presentation based on qualitative input criteria., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name, selector):
    """
    Extracts and returns either the first name or the last name from a full name,
    based on the provided selector.
    
    Parameters:
    - full_name (str): The full name in "Lastname,Firstname" format.
    - selector (str): A string that determines which part of the name to return.
                      '1' for the first name, '2' for the last name.
    
    Returns:
    - str: The selected part of the name (first name or last name).
    """
    # Split the full name by the comma to separate the last name and the first name
    parts = full_name.split(',')
    last_name = parts[0]
    first_name = parts[1]
    
    # Return the appropriate part of the name based on the selector
    if selector == '1':
        return first_name
    elif selector == '2':
        return last_name
    else:
        return "Invalid selector"

# Test cases
# Note: The output of these test cases is not included in this code snippet as per the instructions.
generated_function('Chang,Amy', '1')
generated_function('Chang,Amy', '2')
generated_function('smith,bobby', '2')
generated_function('smith,bobby', '1')
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-09 14:35:19.333630
# Elapsed time in seconds: 9.74694142899898


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

