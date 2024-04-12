# Start time: 2024-04-09 12:43:40.726912

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, each entry formatted as a single string. These names are composed of two main parts: the first name and the last name, separated by a space. The dataset includes a variety of names, indicating a diverse set of individuals. Each name appears to be structured in a Western naming convention, where the first name precedes the last name. The names vary in length and ethnic origin, suggesting a broad representation of people. The input data is qualitative, focusing on the identity of individuals through their names.

### Output Column Summary:

The output column consists of initials derived from the full names provided in the input column. Each entry in the output is formatted as two capital letters separated by a period, representing the first letter of the first name and the first letter of the last name from the input. This transformation reduces the detailed information about the individual's name to a concise and standardized format. The output is also qualitative but offers a more abstract representation of the individual's identity, focusing solely on the initials of their names.

### Relationship Between Input and Output:

The relationship between the input and output columns is a process of abstraction and simplification. The input column's detailed names are transformed into a minimalistic representation in the output column. This transformation involves extracting the first letter of the first and last names from the full name provided in the input, capitalizing these letters, and then presenting them in a standardized format (initials separated by a period). This process maintains a connection to the individual's identity but in a significantly reduced form, making it easier to reference individuals in a concise manner without using their full names. The relationship highlights a method of data simplification and standardization, useful in contexts where detailed personal information is unnecessary or when privacy concerns are paramount., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns the initials of the first and last name.
    
    Parameters:
    full_name (str): The full name of an individual, formatted as "FirstName LastName".
    
    Returns:
    str: The initials of the individual, formatted as "F.L.", where F is the first letter of the first name
         and L is the first letter of the last name.
    """
    # Split the full name into first name and last name
    parts = full_name.split()
    # Extract the first letter of the first name and last name, capitalize them, and format as initials
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

# End time: 2024-04-09 12:43:58.352953
# Elapsed time in seconds: 17.62557377500002