# Start time: 2024-04-09 20:17:49.926105

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names of individuals, each presented in a single string format. These names follow a common pattern where the first name is followed by the last name, separated by a space. The dataset includes a variety of names, indicating a diverse set of individuals. Each name is unique, and the dataset does not show any repetitions or variations of the same name. The names are presented in a standard format, likely representing a formal or official context where full names are required. The diversity in the names suggests a broad representation of different cultures or backgrounds, as indicated by the variety in the structure and phonetics of the names.

### Output Column Summary:

The output data consists of initials derived from the full names provided in the input column. Each output is formatted as two capital letters separated by a period, representing the first letter of the first name and the first letter of the last name from the input data. This format is consistent across all outputs, indicating a standardized method of abbreviation. The output data simplifies the identification of individuals by reducing their full names to initials, which could be useful in contexts where brevity is required, such as in formal documents, lists, or when referencing individuals in a compact format.

### Relationship Between Input and Output:

The relationship between the input and output data is a direct transformation from full names to their corresponding initials. This transformation follows a consistent rule: take the first letter of the first name and the first letter of the last name from the input, capitalize them, and separate them with a period to form the output. This process effectively condenses the qualitative information from a more detailed and personalized format (full names) to a more abstract and concise format (initials). The transformation maintains a link to the original identity of each individual but in a significantly reduced form, which could serve purposes of anonymity, privacy, or simply efficiency in communication and documentation. The method of abbreviation applied here is systematic and can be universally applied to any input following the initial format, making it a reliable way of generating a standardized output from a diverse set of input data., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name.
    
    Parameters:
    full_name (str): The full name of an individual, consisting of the first name and last name separated by a space.
    
    Returns:
    str: The initials of the first and last name, capitalized and separated by a period.
    """
    # Split the full name into first name and last name based on space
    parts = full_name.split()
    # Extract the first letter of the first name and the last name, capitalize them, and join with a period
    initials = f"{parts[0][0].upper()}.{parts[-1][0].upper()}"
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

# End time: 2024-04-09 20:17:58.851853
# Elapsed time in seconds: 8.925560235999


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

