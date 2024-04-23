# Start time: 2024-04-09 16:49:52.564463

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two parts: the first name and the last name, separated by a space. The dataset includes a variety of names, suggesting a diverse set of individuals. Each name is unique, and the structure is consistent across the dataset, adhering to the "FirstName LastName" format. The names appear to be of various ethnic origins, indicating a multicultural dataset. The input data is qualitative, representing categorical, non-numeric information about individuals' names.

### Output Column Summary:

The output column consists of initials derived from the input column's full names. Each entry in the output is formatted as two capital letters separated by a period, representing the first letter of the first name and the first letter of the last name from the input data. This format is consistent across the output dataset, indicating a standardized method of generating initials from full names. The output is also qualitative, providing a simplified, categorical representation of the individuals' names.

### Relationship Between Input and Output:

The relationship between the input and output columns is a transformational one, where the output is a derived, simplified representation of the input data. Specifically, the output initials are generated by taking the first letter of the first name and the first letter of the last name from the input full names, and then formatting these letters as "X.Y.", where X represents the initial of the first name and Y represents the initial of the last name. This process reduces the detailed information available in the input (full names) to a minimalistic identifier (initials), making it easier to reference individuals in a concise manner. The method of generating the output from the input is consistent and follows a clear, predictable pattern. This transformation allows for the preservation of some level of individual identity while significantly reducing the detail and complexity of the data., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name.
    
    Parameters:
    full_name (str): A string containing the first name and last name separated by a space.
    
    Returns:
    str: A string containing the initials of the first and last name, formatted as 'X.Y.', 
         where X is the initial of the first name and Y is the initial of the last name.
    """
    # Split the full name into first name and last name
    parts = full_name.split()
    # Extract the first letter of the first name and the first letter of the last name
    initials = f"{parts[0][0]}.{parts[1][0]}."
    # Convert the initials to uppercase
    return initials.upper()

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: N.F.
print(generated_function('Andrew Cencici'))   # Expected output: A.C.
print(generated_function('Jan Kotas'))        # Expected output: J.K.
print(generated_function('Mariya Sergienko')) # Expected output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-09 16:50:01.060826
# Elapsed time in seconds: 8.496229196000058


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

