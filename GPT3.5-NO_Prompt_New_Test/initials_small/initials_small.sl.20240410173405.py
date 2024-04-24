# Start time: 2024-04-10 17:41:08.698469

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        parts = name.split()
        first_initial = parts[0][0].upper()
        last_initial = parts[1][0].upper()
        return f"{first_initial}.{last_initial}."
    except IndexError:
        return "Invalid input format"

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 17:41:10.764970
# Elapsed time in seconds: 2.0664748970000346


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

