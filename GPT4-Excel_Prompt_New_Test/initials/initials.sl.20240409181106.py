# Start time: 2024-04-09 18:31:08.674264

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of full names, each entry containing a first name followed by a last name. These names appear to be of diverse ethnic origins, indicating a variety of cultural backgrounds. Each entry is structured in a consistent format, with the first name followed by the last name, and both elements are separated by a space. The names are presented in a standard capitalization format, where the first letter of each name is capitalized, and the rest are in lower case. This format suggests a formal or semi-formal context for the data, possibly collected from a professional or academic setting.

### Output Column Summary:

The output data simplifies the input names into initials, following a consistent pattern of taking the first letter of the first name and the first letter of the last name, and separating them with a period. Each output entry corresponds directly to an input entry, maintaining the order and the number of entries. The output is formatted in uppercase, which is a common convention for initials, especially in contexts where brevity and clarity are valued. This transformation from full names to initials reduces the complexity and length of the data while preserving a unique identifier for each entry.

### Relationship Summary:

The transformation from the input to the output column represents a process of data simplification and anonymization. By converting full names into initials, the process retains a level of personal identification while significantly reducing the amount of personal information conveyed. This can be particularly useful in scenarios where privacy is a concern or where space and clarity are at a premium, such as in databases, official documents, or in user interfaces where space is limited.

The relationship between the input and output data is deterministic and follows a clear rule: extract the first letter of the first name and the first letter of the last name, capitalize them if not already, and separate them with a period. This rule applies universally across the dataset, regardless of the length of the names, their cultural origin, or their formatting. This method of data transformation is efficient for creating unique identifiers from more complex personal information, making it a valuable technique in data processing and management., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Simplifies the given full name into initials.
    
    Parameters:
    full_name (str): A string containing a first name and a last name separated by a space.
    
    Returns:
    str: A string containing the initials of the first and last name, separated by a period.
    """
    # Split the full name into first name and last name
    first_name, last_name = full_name.split()
    # Extract the first letter of each name, capitalize them, and join with a period
    initials = f"{first_name[0].upper()}.{last_name[0].upper()}"
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

# End time: 2024-04-09 18:31:23.772632
# Elapsed time in seconds: 15.097915376001765


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

