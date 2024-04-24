# Start time: 2024-04-10 16:06:31.428394

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each full name is composed of a first name and a last name.
- The names vary in length and may have different numbers of characters.
- The input data does not follow a specific pattern or format.

Summary for Output Column Data:
- The output column data consists of initials derived from the input full names.
- Each set of initials consists of the first letter of the first name followed by a period and then the first letter of the last name.
- The initials are in uppercase format and separated by a period.
- The output data is consistent in its format and structure.

Relationship between Input and Output:
- The output column data is derived from the input full names by extracting the first letter of the first name and the first letter of the last name.
- The relationship between the input and output is a transformation process that simplifies the full names into a standardized format of initials.
- The output initials provide a concise representation of the corresponding full names.
- The transformation from full names to initials allows for easier identification and reference of individuals., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    initials = []
    for name in args:
        first_name, last_name = name.split()
        initials.append(f"{first_name[0].upper()}.{last_name[0].upper()}.")
    return initials

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: ['N.F.']
print(generated_function('Andrew Cencici'))    # Output: ['A.C.']
print(generated_function('Jan Kotas'))          # Output: ['J.K.']
print(generated_function('Mariya Sergienko'))   # Output: ['M.S.']
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 16:06:33.289542
# Elapsed time in seconds: 1.861097334999613


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

