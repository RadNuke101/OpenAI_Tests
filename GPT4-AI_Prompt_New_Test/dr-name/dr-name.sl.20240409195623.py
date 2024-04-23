# Start time: 2024-04-09 20:37:06.751738

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in the column is a string that includes a first name followed by a last name, with both names capitalized appropriately. The names appear to be of diverse ethnic origins, indicating a variety of backgrounds. The input data does not include any titles, degrees, or professional designations attached to the names, focusing solely on the personal names of the individuals.

### Output Column Summary:

The output data transforms each input name into a format that prefixes the title "Dr." to the first name of each individual, omitting their last names. This transformation standardizes the output by applying the same professional honorific to all individuals, regardless of their original name structure or cultural background. The output retains the capitalization of the first names and does not alter their spelling. It simplifies the identification by using only the first name followed by the title, thus creating a uniform format across all entries.

### Relationship Between Input and Output:

The relationship between the input and output data is a transformation process that extracts the first name from each full name in the input column and prefixes it with the title "Dr." in the output column. This process signifies an elevation or assignment of a professional or academic title to each individual, suggesting a context where such a title is relevant or desired. The transformation disregards the last names and any potential diversity in background, focusing instead on a uniform application of a professional title to a personal name. This could imply a setting where the recognition of a professional or academic achievement is being highlighted, or where the simplification of names to a title and first name basis is preferred for consistency or ease of reference. The relationship underscores a systematic approach to reformatting personal names into a standardized professional designation., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input and returns a string that prefixes the title "Dr." to the first name,
    omitting the last name.
    
    Parameters:
    full_name (str): A string containing a first name and a last name, separated by a space.
    
    Returns:
    str: A string with the title "Dr." prefixed to the first name.
    """
    # Split the full name into first name and last name
    first_name = full_name.split()[0]
    # Prefix "Dr." to the first name
    output = "Dr. " + first_name
    return output

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 20:37:14.128772
# Elapsed time in seconds: 7.376842821002356


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya


print(generated_function("Carter Liam"))  ### Output: Dr. Carter
print(generated_function("Parker Olivia"))  ### Output: Dr. Parker
print(generated_function("Thompson Mason"))  ### Output: Dr. Thompson
print(generated_function("Turner Jackson"))  ### Output: Dr. Turner
print(generated_function("Reynolds Emma"))  ### Output: Dr. Reynolds
print(generated_function("Bennett Ava"))  ### Output: Dr. Bennett
print(generated_function("Morgan Owen"))  ### Output: Dr. Morgan
print(generated_function("Hayes Benjamin"))  ### Output: Dr. Hayes
print(generated_function("Hayes Gabriel"))  ### Output: Dr. Hayes
print(generated_function("Foster Madison"))  ### Output: Dr. Foster
print(generated_function("Mitchell Caleb"))  ### Output: Dr. Mitchell
print(generated_function("Foster Elijah"))  ### Output: Dr. Foster
print(generated_function("Turner Zoey"))  ### Output: Dr. Turner
print(generated_function("Harrison Grace"))  ### Output: Dr. Harrison
print(generated_function("Davis Wyatt"))  ### Output: Dr. Davis
print(generated_function("Adams Chloe"))  ### Output: Dr. Adams
print(generated_function("Anderson Lily"))  ### Output: Dr. Anderson
print(generated_function("Edwards Carter"))  ### Output: Dr. Edwards
print(generated_function("Smith Logan"))  ### Output: Dr. Smith
print(generated_function("Brooks Isabella"))  ### Output: Dr. Brooks
print(generated_function("Clark Aiden"))  ### Output: Dr. Clark
print(generated_function("Coleman Sophia"))  ### Output: Dr. Coleman
print(generated_function("Johnson Caleb"))  ### Output: Dr. Johnson
print(generated_function("Martin Hannah"))  ### Output: Dr. Martin
print(generated_function("Cooper Nolan"))  ### Output: Dr. Cooper
print(generated_function("Wright Samuel"))  ### Output: Dr. Wright
print(generated_function("Nelson Amelia"))  ### Output: Dr. Nelson
print(generated_function("Cooper Abigail"))  ### Output: Dr. Cooper
print(generated_function("Taylor Harper"))  ### Output: Dr. Taylor
print(generated_function("Walker Scarlett"))  ### Output: Dr. Walker

# TEST SCRIPTS APPENDED!

