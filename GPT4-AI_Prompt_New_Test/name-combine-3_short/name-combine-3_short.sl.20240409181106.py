# Start time: 2024-04-09 19:33:32.731186

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each containing names. The first column includes a variety of first names, while the second column contains last names. The first names span across both genders and exhibit a range of cultural backgrounds, indicating a diverse dataset. The last names also show diversity, suggesting that the dataset does not focus on a specific geographical or cultural group. The names in both columns are proper nouns, used to identify individuals.

### Output Column Summary:

The output data combines elements from both input columns into a single string. The format for the output is the initial of the first name followed by a period and a space, then the full last name. This transformation retains the essential identifying information while abbreviating the first name to its initial. The output format is commonly used in formal and semi-formal contexts, such as professional settings, academic publications, and legal documents, where space or the need for a degree of formality dictates a more concise representation of an individual's name.

### Relationship Summary:

The relationship between the input and output data is a transformation process that condenses the full first name from the input into its initial, adds a period and a space, and then appends the unchanged last name from the input. This process is consistent across all examples, indicating a rule-based transformation that prioritizes brevity and a standardized format for representing names. The transformation does not alter the last name, preserving its full form, which suggests that the last name holds a higher significance or is deemed necessary to be kept intact for identification purposes in the contexts where such a naming convention is applied. This method of name abbreviation facilitates easier sorting, filing, and referencing of names in databases, documents, and communication, where space constraints or the need for uniformity are considerations., and input as ['Launa', 'Withers'] output is L. Withers, input as ['Lakenya', 'Edison'] output is L. Edison, input as ['Brendan', 'Hage'] output is B. Hage, input as ['Bradford', 'Lango'] output is B. Lango, input as ['Rudolf', 'Akiyama'] output is R. Akiyama, input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that combines the initial of the first name with the full last name, formatted
    according to a specific convention (initial of the first name followed by a period
    and a space, then the full last name).
    
    Parameters:
    - first_name (str): The first name of an individual.
    - last_name (str): The last name of an individual.
    
    Returns:
    - str: A string formatted as 'Initial. Lastname'.
    """
    # Extract the initial of the first name and format the output
    output = f"{first_name[0]}. {last_name}"
    return output

# Test cases
print(generated_function('Launa', 'Withers'))  # Expected output: L. Withers
print(generated_function('Lakenya', 'Edison'))  # Expected output: L. Edison
print(generated_function('Brendan', 'Hage'))  # Expected output: B. Hage
print(generated_function('Bradford', 'Lango'))  # Expected output: B. Lango
print(generated_function('Rudolf', 'Akiyama'))  # Expected output: R. Akiyama
print(generated_function('Lara', 'Constable'))  # Expected output: L. Constable
print(generated_function("Launa", "Withers"))  ## Output: L. Withers
print(generated_function("Lakenya", "Edison"))  ## Output: L. Edison
print(generated_function("Brendan", "Hage"))  ## Output: B. Hage
print(generated_function("Bradford", "Lango"))  ## Output: B. Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: R. Akiyama
print(generated_function("Lara", "Constable"))  ## Output: L. Constable

# End time: 2024-04-09 19:33:42.908879
# Elapsed time in seconds: 10.177504376999423


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: L. Withers
print(generated_function("Lakenya", "Edison"))  ## Output: L. Edison
print(generated_function("Brendan", "Hage"))  ## Output: B. Hage
print(generated_function("Bradford", "Lango"))  ## Output: B. Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: R. Akiyama
print(generated_function("Lara", "Constable"))  ## Output: L. Constable


print(generated_function("Olivia", "Parker"))  ### Output: O. Parker
print(generated_function("Elijah", "Foster"))  ### Output: E. Foster
print(generated_function("Abigail", "Cooper"))  ### Output: A. Cooper
print(generated_function("Emma", "Reynolds"))  ### Output: E. Reynolds
print(generated_function("Scarlett", "Walker"))  ### Output: S. Walker
print(generated_function("Benjamin", "Hayes"))  ### Output: B. Hayes
print(generated_function("Samuel", "Wright"))  ### Output: S. Wright
print(generated_function("Carter", "Edwards"))  ### Output: C. Edwards
print(generated_function("Isabella", "Brooks"))  ### Output: I. Brooks
print(generated_function("Sophia", "Coleman"))  ### Output: S. Coleman
print(generated_function("Harper", "Taylor"))  ### Output: H. Taylor
print(generated_function("Mason", "Thompson"))  ### Output: M. Thompson
print(generated_function("Amelia", "Nelson"))  ### Output: A. Nelson
print(generated_function("Aiden", "Clark"))  ### Output: A. Clark
print(generated_function("Caleb", "Johnson"))  ### Output: C. Johnson
print(generated_function("Liam", "Carter"))  ### Output: L. Carter
print(generated_function("Wyatt", "Davis"))  ### Output: W. Davis
print(generated_function("Grace", "Harrison"))  ### Output: G. Harrison
print(generated_function("Owen", "Morgan"))  ### Output: O. Morgan
print(generated_function("Nolan", "Cooper"))  ### Output: N. Cooper
print(generated_function("Gabriel", "Hayes"))  ### Output: G. Hayes
print(generated_function("Hannah", "Martin"))  ### Output: H. Martin
print(generated_function("Jackson", "Turner"))  ### Output: J. Turner
print(generated_function("Madison", "Foster"))  ### Output: M. Foster
print(generated_function("Caleb", "Mitchell"))  ### Output: C. Mitchell
print(generated_function("Ava", "Bennett"))  ### Output: A. Bennett
print(generated_function("Logan", "Smith"))  ### Output: L. Smith
print(generated_function("Chloe", "Adams"))  ### Output: C. Adams
print(generated_function("Lily", "Anderson"))  ### Output: L. Anderson
print(generated_function("Zoey", "Turner"))  ### Output: Z. Turner

# TEST SCRIPTS APPENDED!

