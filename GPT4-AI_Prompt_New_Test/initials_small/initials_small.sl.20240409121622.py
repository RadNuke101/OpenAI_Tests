# Start time: 2024-04-09 13:24:43.253189

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry containing at least a first name and a last name. These names are diverse, representing a variety of cultural backgrounds as indicated by the uniqueness and origin of the surnames and given names. Each name is presented in a standard format, starting with the given name followed by the surname, separated by a space. The names are structured in a way that reflects a common naming convention in many cultures, where an individual's given name precedes their family name. The dataset does not include middle names or initials, focusing solely on the primary components of a person's identity: their first and last names. This simplicity in structure allows for a straightforward analysis and processing of the data.

### Output Column Summary:

The output column contains initials derived from the full names listed in the input column. Each entry in the output is formatted as two capital letters separated by a period, where the first letter represents the first initial of the given name, and the second letter represents the initial of the surname. This output format standardizes the representation of names, reducing them to their simplest alphanumeric identifiers. The use of initials and the inclusion of a period for separation provide a concise, universally understandable format. This method of abbreviation is commonly used in various contexts to refer to individuals in a more formal or anonymized manner.

### Relationship Summary:

The relationship between the input and output columns is a direct transformation of the full names into their corresponding initials. This process involves extracting the first letter from both the given name and the surname of each individual, capitalizing these letters, and then combining them with a period separator. This transformation serves to anonymize or formalize the names, making them suitable for contexts where brevity or privacy is desired. The method is consistent across all entries, indicating a standardized approach to generating initials from full names. This relationship highlights a common practice in data processing where detailed personal information is condensed into a more manageable form, preserving essential identity markers while omitting specifics., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the given name and surname,
    formatted as two capital letters separated by a period.
    
    :param full_name: A string containing a given name and a surname separated by a space.
    :return: A string containing the initials of the given name and surname.
    """
    # Split the full name into given name and surname
    name_parts = full_name.split()
    # Extract the first letter of the given name and surname, capitalize them, and format with a period
    initials = f"{name_parts[0][0].upper()}.{name_parts[1][0].upper()}."
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

# End time: 2024-04-09 13:24:50.938050
# Elapsed time in seconds: 7.684639807999702


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.


print(generated_function("Carter Edwards"))  ### Output: C.E.
print(generated_function("Hannah Martin"))  ### Output: H.M.
print(generated_function("Grace Harrison"))  ### Output: G.H.
print(generated_function("Logan Smith"))  ### Output: L.S.
print(generated_function("Olivia Parker"))  ### Output: O.P.
print(generated_function("Mason Thompson"))  ### Output: M.T.
print(generated_function("Caleb Johnson"))  ### Output: C.J.
print(generated_function("Gabriel Hayes"))  ### Output: G.H.
print(generated_function("Benjamin Hayes"))  ### Output: B.H.
print(generated_function("Chloe Adams"))  ### Output: C.A.
print(generated_function("Ava Bennett"))  ### Output: A.B.
print(generated_function("Aiden Clark"))  ### Output: A.C.
print(generated_function("Liam Carter"))  ### Output: L.C.
print(generated_function("Zoey Turner"))  ### Output: Z.T.
print(generated_function("Emma Reynolds"))  ### Output: E.R.
print(generated_function("Samuel Wright"))  ### Output: S.W.
print(generated_function("Wyatt Davis"))  ### Output: W.D.
print(generated_function("Sophia Coleman"))  ### Output: S.C.
print(generated_function("Nolan Cooper"))  ### Output: N.C.
print(generated_function("Madison Foster"))  ### Output: M.F.
print(generated_function("Lily Anderson"))  ### Output: L.A.
print(generated_function("Owen Morgan"))  ### Output: O.M.
print(generated_function("Scarlett Walker"))  ### Output: S.W.
print(generated_function("Caleb Mitchell"))  ### Output: C.M.
print(generated_function("Isabella Brooks"))  ### Output: I.B.
print(generated_function("Jackson Turner"))  ### Output: J.T.
print(generated_function("Elijah Foster"))  ### Output: E.F.
print(generated_function("Harper Taylor"))  ### Output: H.T.
print(generated_function("Amelia Nelson"))  ### Output: A.N.
print(generated_function("Abigail Cooper"))  ### Output: A.C.

# TEST SCRIPTS APPENDED!

