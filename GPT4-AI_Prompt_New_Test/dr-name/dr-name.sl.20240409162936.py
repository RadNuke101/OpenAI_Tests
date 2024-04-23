# Start time: 2024-04-09 17:07:11.137874

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of full names, each comprising at least a first name and a last name. These names represent individuals, likely from various cultural or ethnic backgrounds, as indicated by the diversity in the surnames. The names are presented in a standard format, with the first name followed by the last name, and each name is contained within a single list element. This format suggests that the data could be personal names from a database, a list of members in an organization, or participants in a study. The names do not include any titles or honorifics, focusing solely on the personal and family names of the individuals.

### Output Column Summary:

The output data transforms each input name into a formal address, specifically by appending the title "Dr." to the first name of each individual. This transformation suggests a formal or professional context where the individuals are being recognized or addressed with a title of respect or academic/professional achievement. The output retains only the first name from the input and discards the last name, indicating a selective emphasis on personal identification rather than familial or heritage aspects. The uniform application of the title "Dr." across diverse names implies a universal acknowledgment of status or role, rather than a reflection of personal characteristics or backgrounds.

### Relationship Summary:

The relationship between the input and output data demonstrates a process of formalization and professionalization of personal names. By appending the title "Dr." to the first names, the transformation suggests an elevation of status or the acknowledgment of an academic or professional achievement associated with each individual. This process selectively focuses on the personal aspect of each name, emphasizing individual identity within a formal or professional context. The omission of last names in the output highlights a shift from a personal-familial identity to a role-based identity, where the title "Dr." serves as a universal marker of respect, achievement, or authority. The consistent application of this transformation across a diverse set of names indicates a standardized approach to addressing or recognizing individuals in a specific context, possibly related to academia, medicine, or another field where such titles are customary., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns a formal address
    by appending the title "Dr." to the first name, discarding the last name.
    
    Parameters:
    full_name (str): A string containing the first name and last name of an individual.
    
    Returns:
    str: A string containing the formal address with the title "Dr." appended to the first name.
    """
    # Split the full name into first name and last name
    first_name = full_name.split()[0]
    
    # Append the title "Dr." to the first name
    formal_address = "Dr. " + first_name
    
    return formal_address

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))   # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))        # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko')) # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 17:07:22.815405
# Elapsed time in seconds: 11.677319260998047


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya


print(generated_function("Carter Liam"))  ### Output: Dr. Carter
print(generated_function("Parker Olivia"))  ### Output: Dr. Parker
print(generated_function("Thompson Mason"))  ### Output: Dr. Thompson
print(generated_function("Turner Jackson"))  ### Output: Dr. Turner
print(generated_function("Reynolds Emma"))  ### Output: Dr. Reynolds
print(generated_function("Bennett Ava"))  ### Output: Dr. Bennett
print(generated_function("Morgan Owen"))  ### Output: Dr. Morgan
print(generated_function("Hayes Benjamin"))  ### Output: Dr. Hayes
print(generated_function("Hayes Gabriel"))  ### Output: Dr. Hayes
print(generated_function("Foster Madison"))  ### Output: Dr. Foster
print(generated_function("Mitchell Caleb"))  ### Output: Dr. Mitchell
print(generated_function("Foster Elijah"))  ### Output: Dr. Foster
print(generated_function("Turner Zoey"))  ### Output: Dr. Turner
print(generated_function("Harrison Grace"))  ### Output: Dr. Harrison
print(generated_function("Davis Wyatt"))  ### Output: Dr. Davis
print(generated_function("Adams Chloe"))  ### Output: Dr. Adams
print(generated_function("Anderson Lily"))  ### Output: Dr. Anderson
print(generated_function("Edwards Carter"))  ### Output: Dr. Edwards
print(generated_function("Smith Logan"))  ### Output: Dr. Smith
print(generated_function("Brooks Isabella"))  ### Output: Dr. Brooks
print(generated_function("Clark Aiden"))  ### Output: Dr. Clark
print(generated_function("Coleman Sophia"))  ### Output: Dr. Coleman
print(generated_function("Johnson Caleb"))  ### Output: Dr. Johnson
print(generated_function("Martin Hannah"))  ### Output: Dr. Martin
print(generated_function("Cooper Nolan"))  ### Output: Dr. Cooper
print(generated_function("Wright Samuel"))  ### Output: Dr. Wright
print(generated_function("Nelson Amelia"))  ### Output: Dr. Nelson
print(generated_function("Cooper Abigail"))  ### Output: Dr. Cooper
print(generated_function("Taylor Harper"))  ### Output: Dr. Taylor
print(generated_function("Walker Scarlett"))  ### Output: Dr. Walker

# TEST SCRIPTS APPENDED!

