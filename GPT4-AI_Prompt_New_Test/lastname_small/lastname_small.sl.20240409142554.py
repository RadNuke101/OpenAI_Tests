# Start time: 2024-04-09 14:55:58.314767

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are structured in the traditional Western naming convention, where each entry is composed of a first name followed by a last name, separated by a space. The dataset includes a variety of names, indicating a diverse set of individuals. The names appear to be of various ethnic origins, suggesting a multicultural dataset. Each entry is unique, and there are no repetitions of the same name, indicating a sample of distinct individuals.

### Output Column Summary:

The output column contains the last names extracted from the full names provided in the input column. Each entry in the output is a single word, representing the family name or surname of the individual mentioned in the corresponding input entry. The output retains the diversity of the input, showcasing a range of surnames that hint at the multicultural background of the dataset. There are no prefixes or suffixes attached to these surnames, and they are presented in their simplest form.

### Relationship Summary:

The relationship between the input and output columns is straightforward: the output is derived directly from the input by extracting the last name from each full name. This process involves identifying the space that separates the first name from the last name in the input and then selecting the portion of the string that follows this space. The transformation from input to output does not alter the spelling or formatting of the last names, ensuring that the integrity of the original data is maintained. This relationship highlights a methodical extraction process focused on isolating a specific component (the surname) from a more complex data structure (the full name), which could be useful for tasks that require identification or categorization based on family names., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts and returns the last name from a full name.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: The last name extracted from the full name.
    """
    # Split the full name into parts and return the last part (surname)
    return full_name.split(" ")[-1]

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: FreeHafer
print(generated_function('Andrew Cencici'))  # Expected output: Cencici
print(generated_function('Jan Kotas'))  # Expected output: Kotas
print(generated_function('Mariya Sergienko'))  # Expected output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-09 14:56:03.944535
# Elapsed time in seconds: 5.629701859999841


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko


print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Scarlett Walker"))  ### Output: Walker
print(generated_function("Caleb Johnson"))  ### Output: Johnson
print(generated_function("Amelia Nelson"))  ### Output: Nelson
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Jackson Turner"))  ### Output: Turner
print(generated_function("Gabriel Hayes"))  ### Output: Hayes
print(generated_function("Isabella Brooks"))  ### Output: Brooks
print(generated_function("Zoey Turner"))  ### Output: Turner
print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Carter Edwards"))  ### Output: Edwards
print(generated_function("Madison Foster"))  ### Output: Foster
print(generated_function("Harper Taylor"))  ### Output: Taylor
print(generated_function("Ava Bennett"))  ### Output: Bennett
print(generated_function("Nolan Cooper"))  ### Output: Cooper
print(generated_function("Abigail Cooper"))  ### Output: Cooper
print(generated_function("Lily Anderson"))  ### Output: Anderson
print(generated_function("Hannah Martin"))  ### Output: Martin
print(generated_function("Owen Morgan"))  ### Output: Morgan
print(generated_function("Chloe Adams"))  ### Output: Adams
print(generated_function("Wyatt Davis"))  ### Output: Davis
print(generated_function("Elijah Foster"))  ### Output: Foster
print(generated_function("Sophia Coleman"))  ### Output: Coleman
print(generated_function("Samuel Wright"))  ### Output: Wright
print(generated_function("Logan Smith"))  ### Output: Smith
print(generated_function("Liam Carter"))  ### Output: Carter
print(generated_function("Mason Thompson"))  ### Output: Thompson
print(generated_function("Aiden Clark"))  ### Output: Clark
print(generated_function("Grace Harrison"))  ### Output: Harrison

# TEST SCRIPTS APPENDED!

