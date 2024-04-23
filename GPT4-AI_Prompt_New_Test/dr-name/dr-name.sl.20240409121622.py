# Start time: 2024-04-09 13:04:31.821921

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of full names, each entry comprising a first name followed by a last name. These names represent individuals without any explicit titles or qualifications attached to them. The names are diverse, suggesting a variety of cultural or ethnic backgrounds. Each entry is structured in a consistent format, with the first name leading, followed by the last name, and each name is capitalized appropriately. The data appears to be personal names, likely representing a group of people, without any additional context or information provided.

### Output Column Summary:

The output data transforms each input name by retaining only the first name and prefixing it with the title "Dr." This modification suggests an elevation or assignment of a professional or academic status to each individual. The last names are omitted in the output, focusing solely on the first names and the newly assigned title. This transformation uniformly applies to all entries, regardless of the original name's cultural or ethnic background, implying a standardized process of title assignment.

### Relationship Between Input and Output:

The relationship between the input and output data is a process of transformation that assigns a professional or academic title to each individual, based solely on their first name. This process involves two key steps: (1) extracting the first name from the full name provided in the input, and (2) prefixing this first name with the title "Dr." to generate the output. The transformation disregards the last names and any potential cultural or ethnic significance they might carry, focusing instead on a universal application of a professional title. This suggests an intention to either simulate or prepare data for a context where the professional status of individuals (indicated by the title "Dr.") is relevant, while their specific identity (as indicated by the full name) is of lesser importance. The consistent application of this transformation across a diverse set of names indicates a standardized approach to assigning professional titles, possibly for a hypothetical or illustrative purpose., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    This function takes a full name as input, extracts the first name, and prefixes it with "Dr." to generate the output.
    
    Parameters:
    - full_name (str): A string containing the first name followed by the last name, separated by a space.
    
    Returns:
    - str: A string with the first name prefixed by "Dr.".
    """
    # Split the full name into first name and last name
    first_name = full_name.split()[0]
    # Prefix the first name with "Dr." and return the result
    return "Dr. " + first_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-09 13:04:42.264353
# Elapsed time in seconds: 10.44224584099993


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

