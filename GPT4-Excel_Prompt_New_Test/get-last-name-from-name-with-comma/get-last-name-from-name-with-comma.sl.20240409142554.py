# Start time: 2024-04-09 14:41:14.271488

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing strings that represent names in the format "lastname,firstname". Each entry is a combination of a last name and a first name of an individual, separated by a comma. The names are diverse, indicating a variety of individuals. The format is consistent across all entries, adhering to the "lastname,firstname" structure without any deviations. This format suggests a structured approach to capturing names, possibly for sorting or organizing purposes based on last names.

### Output Column Summary:

The output data transforms the format of the names from the input column into "firstname,lastname". This reversal indicates a reorientation of the data to prioritize first names over last names. The output retains the integrity of the names, ensuring that each first name is correctly matched with its corresponding last name. The transformation does not alter the names themselves but changes their presentation order. This suggests an intention to personalize or make the data more accessible by foregrounding first names.

### Relationship Between Input and Output:

The relationship between the input and output data is characterized by a simple yet systematic transformation of the format in which individual names are presented. The process involves reversing the order of the first and last names while maintaining the integrity of the names. This transformation could be driven by the need to adapt the data for different contexts where first names are preferred for identification or interaction purposes. The consistent structure in both input and output suggests a deliberate effort to maintain data quality and readability, facilitating easy conversion between formats. The transformation does not add, remove, or alter the names themselves, indicating a focus on reformatting rather than modifying the content. This relationship highlights the flexibility of data presentation and the importance of format in data management and utilization., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    This function takes a string representing a name in the format "lastname,firstname"
    and transforms it into the format "firstname,lastname".
    
    :param name: A string containing a name in the format "lastname,firstname"
    :return: A string containing the name in the format "firstname,lastname"
    """
    # Split the input string into two parts: lastname and firstname
    parts = name.split(',')
    # Reverse the order and join them back together
    transformed_name = parts[1] + ',' + parts[0]
    return transformed_name

# Test cases
print(generated_function('chang,amy'))  # Expected output: amy,chang
print(generated_function('smith,bobby'))  # Expected output: bobby,smith
print(generated_function('lennox,aaron'))  # Expected output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-09 14:41:22.105458
# Elapsed time in seconds: 7.833940757000164


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!

