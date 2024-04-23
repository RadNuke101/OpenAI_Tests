# Start time: 2024-04-09 15:30:43.352692

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are structured in a conventional Western format, where each entry typically includes a given name followed by a surname, separated by a space. The dataset includes a variety of names, suggesting a diverse set of individuals. The names are composed of alphabetic characters, and each name varies in length and cultural origin, indicating a broad representation of different backgrounds. The input data is qualitative, representing categorical, non-numeric information about individuals' identities.

### Output Column Summary:

The output column consists of initials derived from the full names provided in the input column. Each entry in the output is formatted as two capital letters, each followed by a period, and the two are separated by a space. These initials correspond to the first letter of the given name and the first letter of the surname from the input data. The output retains the capitalization of the initial letters, ensuring a standardized format across all entries. This transformation reduces the detailed information about individuals' names to a minimal, anonymized form, focusing solely on the initials of their given name and surname.

### Relationship Between Input and Output:

The relationship between the input and output columns is a process of reduction and abstraction, where the detailed, qualitative information about an individual's full name is condensed into a simplified, anonymized form represented by the initials. This process involves extracting the first letter of the given name and the first letter of the surname from the full name provided in the input, and then formatting these letters as initials in the output. The transformation maintains a direct, deterministic link between the input and output, where the output is entirely dependent on the specific characters present in the input data. This method of summarization preserves a trace of the individual's identity while significantly reducing the amount of personal information conveyed, making it a useful technique for contexts requiring privacy or brevity., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the given name and surname,
    formatted as two capital letters, each followed by a period, and separated by a space.
    """
    # Split the full name into given name and surname
    parts = full_name.split()
    # Extract the first letter of the given name and surname, capitalize them, and format as required
    initials = f"{parts[0][0].upper()}.{parts[1][0].upper()}."
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

# End time: 2024-04-09 15:30:52.191101
# Elapsed time in seconds: 8.838235543000337


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

