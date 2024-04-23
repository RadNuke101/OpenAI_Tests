# Start time: 2024-04-09 16:16:36.194961

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names, which are strings that include first names, middle names or initials, and last names. These names are diverse, representing a variety of cultural backgrounds as indicated by the structure and phonetics of the names. The names may also include middle initials followed by a period or full middle names, and in some cases, two middle names or a compound last name. The structure of these names varies, indicating no strict format is followed other than the inclusion of at least a first name and a last name. The diversity in the names suggests a broad representation of individuals, possibly from different regions or ethnic backgrounds.

### Output Column Summary:

The output column extracts and presents the middle names or initials from the input names, where applicable. In cases where there are no middle names or initials, the output is left blank. When the input includes a middle initial, it is preserved in the output along with the period. For inputs with full middle names, these are provided in the output. In the case of inputs with two middle names or initials, both are included in the output. The output strictly focuses on the middle segment(s) of the names, disregarding first and last names entirely.

### Relationship Summary:

The relationship between the input and output columns is defined by the extraction process of middle names or initials from the full names provided in the input. The output is specifically tailored to capture and isolate the middle portion(s) of the names, which can be a single middle name, a middle initial, or two middle names/initials. This process highlights a selective focus on the middle component of personal names, effectively ignoring the first and last names for the purpose of the output.

This extraction process suggests an analytical interest in the middle names or initials, which could be for reasons such as identifying patterns, understanding naming conventions across cultures, or simply separating these components for further analysis or database structuring. The method is consistent across varied name structures, indicating a robust approach to identifying and isolating the middle segments of full names regardless of their complexity or cultural background., and input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the middle name(s) or initial(s) from a full name string.
    
    Parameters:
    full_name (str): A string containing a full name which may include first name, middle name(s) or initial(s), and last name.
    
    Returns:
    str: The extracted middle name(s) or initial(s). Returns an empty string if there are no middle names or initials.
    """
    # Split the full name into parts based on spaces
    name_parts = full_name.split()
    
    # If the name consists of only two parts (first and last name), return an empty string
    if len(name_parts) <= 2:
        return ""
    
    # If the name consists of more than two parts, return the middle part(s) as a string
    # Joining the middle parts with a space in case of two middle names or initials
    return ' '.join(name_parts[1:-1])

# Test cases
print(generated_function('susan ann chang'))  # Expected output: ann
print(generated_function('ayako tanaka'))  # Expected output: (empty string)
print(generated_function('bobby t. smith'))  # Expected output: t.
print(generated_function('anthory r. tom brown'))  # Expected output: r. tom
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-09 16:16:48.037672
# Elapsed time in seconds: 11.842622562999168


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

