# Start time: 2024-04-09 19:44:11.016292

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, which are strings that include first names, middle names or initials, and last names. These names are presented in a variety of formats, reflecting a diversity in the naming conventions. Some names include middle initials followed by a period (e.g., 'bobby t. smith'), while others include full middle names (e.g., 'susan ann chang'). There are also instances where multiple middle names or initials are present (e.g., 'anthory r. tom brown'). The names come from a range of cultural backgrounds, as indicated by the variety in the structure and origin of the names (e.g., 'ayako tanaka' suggests a Japanese origin, while 'susan ann chang' might indicate a Western or Chinese background). The input data is qualitative, focusing on the composition and structure of individual names.

### Output Column Summary:

The output column extracts and presents the middle names or initials from the full names provided in the input column. In cases where there are middle initials, they are preserved along with the period (e.g., 't.' from 'bobby t. smith'). When there are full middle names, they are extracted in their entirety (e.g., 'ann' from 'susan ann chang'). For names with multiple middle names or initials, all are included in the output (e.g., 'r. tom' from 'anthory r. tom brown'). However, if a name does not appear to have a middle name or initial, the output is left blank (e.g., the output for 'ayako tanaka' is empty). This suggests a focus on identifying and isolating the middle segment(s) of the provided full names, regardless of their format or the cultural origin of the name.

### Relationship Summary:

The relationship between the input and output columns is defined by the extraction process of middle names or initials from the full names provided. The output is directly dependent on the structure and composition of the input names. The process respects the original formatting of the names, including the preservation of periods after initials and the inclusion of all middle names or initials when multiple are present. The extraction process does not alter the original names but isolates a specific component (the middle name(s) or initial(s)) based on its position within the full name. This relationship highlights a systematic approach to identifying and presenting a specific part of a qualitative data set, focusing on the internal structure of the data (in this case, the names) to extract meaningful information (the middle names or initials)., and input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the middle name(s) or initial(s) from a given full name.
    
    :param full_name: A string representing a full name which may include first name, middle name(s) or initial(s), and last name.
    :return: A string containing the middle name(s) or initial(s) extracted from the full name. Returns an empty string if no middle name or initial is found.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.split()
    
    # If the name consists of only two parts (likely first and last name), return an empty string as there's no middle name or initial
    if len(name_parts) <= 2:
        return ""
    
    # Extract the middle name(s) or initial(s) by excluding the first and last parts of the name
    middle_parts = name_parts[1:-1]
    
    # Join the middle parts back into a string and return it
    return ' '.join(middle_parts)

# Test cases
print(generated_function('susan ann chang'))  # Expected output: 'ann'
print(generated_function('ayako tanaka'))     # Expected output: ''
print(generated_function('bobby t. smith'))   # Expected output: 't.'
print(generated_function('anthory r. tom brown'))  # Expected output: 'r. tom'
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-09 19:44:19.824852
# Elapsed time in seconds: 8.808396592998179


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

