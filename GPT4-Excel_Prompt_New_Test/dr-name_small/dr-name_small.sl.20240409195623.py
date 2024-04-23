# Start time: 2024-04-09 21:14:32.848921

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of a series of full names, each entry containing a first name followed by a last name. These names represent individuals, likely from diverse backgrounds given the variety of name origins (e.g., "Nancy FreeHafer," "Andrew Cencici," "Jan Kotas," "Mariya Sergienko"). The names are presented in a standard format, with the first name preceding the last name, and each name is capitalized appropriately, indicating a formal or official listing of names. The data does not include any titles, middle names, or additional identifiers, focusing solely on the primary given name and the family name.

### Output Column Summary:

The output column simplifies the input data by extracting only the first name from each entry and prefixing it with the title "Dr." This transformation uniformly applies a professional or academic honorific to each individual, regardless of their original name's cultural background or the gender associated with the first name. The output retains the capitalization of the first name and follows a consistent format: "Dr. [First Name]." This suggests a standardization or formalization process, possibly indicating a professional setting or an academic context where such titles are relevant.

### Relationship Between Input and Output:

The relationship between the input and output columns is a process of extraction and transformation. From each full name in the input column, the first name is extracted, and a title ("Dr.") is prefixed to it, creating a new representation of the name that emphasizes professional or academic status. This process strips away the last names, removing a layer of personal identity related to family or heritage, and replaces it with a universal marker of respect and achievement. The transformation does not alter the first names themselves, preserving the individual's personal identity to some extent while elevating their status uniformly across the dataset. This suggests a purposeful recontextualization of the individuals from a possibly more personal or informal setting to one that is professional or academic, where titles play a significant role in identity and status., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Extracts the first name from a full name and prefixes it with 'Dr.'.

    Parameters:
    full_name (str): A string containing a first name followed by a last name.

    Returns:
    str: A string with the first name prefixed by 'Dr.'.
    """
    # Split the full name into parts
    name_parts = full_name.split()
    # Extract the first name
    first_name = name_parts[0]
    # Prefix the first name with 'Dr.' and return
    return f"Dr. {first_name}"

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 21:14:41.648635
# Elapsed time in seconds: 8.799458736000815


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya


print(generated_function("Smith Logan"))  ### Output: Dr. Smith
print(generated_function("Anderson Lily"))  ### Output: Dr. Anderson
print(generated_function("Carter Liam"))  ### Output: Dr. Carter
print(generated_function("Parker Olivia"))  ### Output: Dr. Parker
print(generated_function("Hayes Gabriel"))  ### Output: Dr. Hayes
print(generated_function("Foster Madison"))  ### Output: Dr. Foster
print(generated_function("Martin Hannah"))  ### Output: Dr. Martin
print(generated_function("Reynolds Emma"))  ### Output: Dr. Reynolds
print(generated_function("Foster Elijah"))  ### Output: Dr. Foster
print(generated_function("Clark Aiden"))  ### Output: Dr. Clark
print(generated_function("Coleman Sophia"))  ### Output: Dr. Coleman
print(generated_function("Adams Chloe"))  ### Output: Dr. Adams
print(generated_function("Cooper Abigail"))  ### Output: Dr. Cooper
print(generated_function("Turner Jackson"))  ### Output: Dr. Turner
print(generated_function("Turner Zoey"))  ### Output: Dr. Turner
print(generated_function("Bennett Ava"))  ### Output: Dr. Bennett
print(generated_function("Brooks Isabella"))  ### Output: Dr. Brooks
print(generated_function("Thompson Mason"))  ### Output: Dr. Thompson
print(generated_function("Johnson Caleb"))  ### Output: Dr. Johnson
print(generated_function("Taylor Harper"))  ### Output: Dr. Taylor
print(generated_function("Nelson Amelia"))  ### Output: Dr. Nelson
print(generated_function("Edwards Carter"))  ### Output: Dr. Edwards
print(generated_function("Mitchell Caleb"))  ### Output: Dr. Mitchell
print(generated_function("Harrison Grace"))  ### Output: Dr. Harrison
print(generated_function("Davis Wyatt"))  ### Output: Dr. Davis
print(generated_function("Walker Scarlett"))  ### Output: Dr. Walker
print(generated_function("Morgan Owen"))  ### Output: Dr. Morgan
print(generated_function("Hayes Benjamin"))  ### Output: Dr. Hayes
print(generated_function("Cooper Nolan"))  ### Output: Dr. Cooper
print(generated_function("Wright Samuel"))  ### Output: Dr. Wright

# TEST SCRIPTS APPENDED!

