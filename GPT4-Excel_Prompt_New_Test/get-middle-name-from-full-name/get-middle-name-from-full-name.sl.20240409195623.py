# Start time: 2024-04-09 21:35:27.287788

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names of individuals, which are structured in a variety of formats. These names are presented as single strings within an array, and each name typically includes a first name, a middle name or initial, and a last name. However, the structure is not uniform across all entries. Some names may include multiple middle names or initials, while others might not have a middle name at all. The diversity in the structure of these names suggests a need to identify and extract specific components from these strings, based on certain criteria.

### Output Column Summary:

The output data extracts and presents the middle name or initials from the given full names in the input column. When a name includes a middle name or initial, it is isolated and provided as the output. In cases where the name does not include a middle name or initial, the output is left blank. The output demonstrates a selective extraction based on the presence of middle names or initials within the full names provided in the input. This extraction does not uniformly apply to all entries, as it is contingent on the specific structure of each name.

### Relationship Summary:

The relationship between the input and output data is characterized by the process of identifying and extracting middle names or initials from full names. The output is directly dependent on the structure of the input names; it selectively captures the middle component(s) of the name, if present. This process highlights a focused interest in the middle segment of the names, which can vary significantly from one entry to another in terms of presence and format (e.g., a single middle name, multiple middle names, or initials). The extraction process respects the original formatting of the names, including the retention of periods after initials, and it adapts to the variability in name structures, demonstrating a tailored approach to each entry based on its unique composition., and input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the middle name(s) or initial(s) from a given full name.
    If there is no middle name or initial, returns an empty string.
    
    :param full_name: A string containing the full name of an individual.
    :return: A string containing the middle name(s) or initial(s), or an empty string if none.
    """
    # Split the full name into parts
    name_parts = full_name.split()
    
    # If there are more than two parts (first and last name), extract the middle part(s)
    if len(name_parts) > 2:
        # Join the middle part(s) and return
        return ' '.join(name_parts[1:-1])
    else:
        # No middle name or initial, return an empty string
        return ''

# Test cases
print(generated_function('susan ann chang'))  # Expected output: 'ann'
print(generated_function('ayako tanaka'))     # Expected output: ''
print(generated_function('bobby t. smith'))   # Expected output: 't.'
print(generated_function('anthory r. tom brown'))  # Expected output: 'r. tom'
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-09 21:35:35.389572
# Elapsed time in seconds: 8.10171289400023


# APPEND TEST SCRIPTS...
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom


print(generated_function("olivia parker"))  ### Output: 
print(generated_function("emma von reynolds"))  ### Output: von
print(generated_function("caleb mitchell"))  ### Output: 
print(generated_function("grace f. harrison"))  ### Output: f.
print(generated_function("mason ann thompson"))  ### Output: ann
print(generated_function("wyatt thomas davis"))  ### Output: thomas
print(generated_function("jackson ann turner"))  ### Output: ann
print(generated_function("benjamin t. hayes"))  ### Output: t.
print(generated_function("lily anderson"))  ### Output: 

# TEST SCRIPTS APPENDED!

