# Start time: 2024-04-10 13:28:53.846990

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period, and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to return the desired output format
def generated_function(input_str):
    # Split the input string into words
    words = input_str.split()
    
    # Extract the first letter of each word and format the output
    output = words[0][0] + '.' + words[1][0] + '.'
    
    return output

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 13:28:55.728424
# Elapsed time in seconds: 1.8813918969999577


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

