# Start time: 2024-04-09 14:51:32.975503

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are structured in the traditional Western naming convention, comprising at least a first name and a last name, separated by a space. The dataset includes a variety of names, indicating a diverse set of individuals. Each name is unique, suggesting a one-to-one mapping from the input to the output. The names appear to be personal names, possibly representing a sample from a larger population. The diversity in the names suggests a wide range of cultural backgrounds.

### Output Column Summary:

The output column contains initials derived from the corresponding full names in the input column. Each entry in the output is formatted as two capital letters separated by a period, representing the first letter of the first name and the first letter of the last name from the input. This format is consistent across all entries, indicating a standardized method of generating outputs from the inputs. The output retains no information about the middle names or any additional names that might be part of the full names in the input.

### Relationship Summary:

The relationship between the input and output columns is a transformation process where each full name from the input is converted into a set of initials in the output. This process involves extracting the first letter of the first name and the first letter of the last name from each full name in the input, capitalizing these letters, and then combining them with a period in between. This transformation is deterministic and consistent, meaning the same input will always produce the same output. The method does not account for middle names, suffixes, or prefixes in the names, focusing solely on the first and last names. This relationship highlights a simplification or abstraction of personal identity from a full name to a minimal representation using initials, which could be used for purposes where brevity or anonymity is desired., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name.
    
    Parameters:
    full_name (str): The full name of an individual, formatted as "FirstName LastName".
    
    Returns:
    str: The initials of the first and last name, formatted as "F.L.".
    """
    # Split the full name into a list of names
    names = full_name.split()
    # Extract the first letter of the first name and the last name, capitalize them, and format as initials
    initials = f"{names[0][0].upper()}.{names[-1][0].upper()}."
    return initials

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: N.F.
print(generated_function('Andrew Cencici'))  # Expected output: A.C.
print(generated_function('Jan Kotas'))  # Expected output: J.K.
print(generated_function('Mariya Sergienko'))  # Expected output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-09 14:51:41.779815
# Elapsed time in seconds: 8.804275721999147


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.


print(generated_function("Mason Thompson"))  ### Output: M.T.
print(generated_function("Scarlett Walker"))  ### Output: S.W.
print(generated_function("Logan Smith"))  ### Output: L.S.
print(generated_function("Samuel Wright"))  ### Output: S.W.
print(generated_function("Gabriel Hayes"))  ### Output: G.H.
print(generated_function("Abigail Cooper"))  ### Output: A.C.
print(generated_function("Zoey Turner"))  ### Output: Z.T.
print(generated_function("Carter Edwards"))  ### Output: C.E.
print(generated_function("Lily Anderson"))  ### Output: L.A.
print(generated_function("Benjamin Hayes"))  ### Output: B.H.
print(generated_function("Olivia Parker"))  ### Output: O.P.
print(generated_function("Grace Harrison"))  ### Output: G.H.
print(generated_function("Sophia Coleman"))  ### Output: S.C.
print(generated_function("Aiden Clark"))  ### Output: A.C.
print(generated_function("Liam Carter"))  ### Output: L.C.
print(generated_function("Wyatt Davis"))  ### Output: W.D.
print(generated_function("Elijah Foster"))  ### Output: E.F.
print(generated_function("Hannah Martin"))  ### Output: H.M.
print(generated_function("Jackson Turner"))  ### Output: J.T.
print(generated_function("Caleb Johnson"))  ### Output: C.J.
print(generated_function("Isabella Brooks"))  ### Output: I.B.
print(generated_function("Amelia Nelson"))  ### Output: A.N.
print(generated_function("Caleb Mitchell"))  ### Output: C.M.
print(generated_function("Chloe Adams"))  ### Output: C.A.
print(generated_function("Madison Foster"))  ### Output: M.F.
print(generated_function("Nolan Cooper"))  ### Output: N.C.
print(generated_function("Ava Bennett"))  ### Output: A.B.
print(generated_function("Owen Morgan"))  ### Output: O.M.
print(generated_function("Harper Taylor"))  ### Output: H.T.
print(generated_function("Emma Reynolds"))  ### Output: E.R.

# TEST SCRIPTS APPENDED!

