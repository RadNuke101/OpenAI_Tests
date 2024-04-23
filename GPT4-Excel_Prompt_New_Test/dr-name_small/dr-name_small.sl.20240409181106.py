# Start time: 2024-04-09 19:24:27.140127

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of names, each presented in a single format: first name followed by last name. These names represent individuals, with no specific pattern regarding gender, nationality, or any other demographic characteristic. Each entry is unique and appears to be a personal name, likely representing a diverse group of individuals. The names are presented in a straightforward, unabbreviated form, providing a clear and direct identification of each person.

### Output Column Summary:

The output data transforms each input name into a formal title, specifically by prefixing each first name with "Dr." This transformation maintains the first name of each individual from the input data while discarding the last name. The output uniformly applies the honorific "Dr." to all individuals, suggesting a conferred level of respect or academic/professional achievement. The output is consistent in its format, applying the same modification to each entry without variation.

### Relationship Summary:

The relationship between the input and output data is a systematic transformation that applies a formal academic or professional title to each individual's name. This process involves two key steps: retaining the first name from the input and prefixing it with the title "Dr." The transformation suggests a context where the individuals' professional or academic status is being emphasized or acknowledged, possibly for a setting where such titles are relevant or required. The process does not discriminate based on the original name's characteristics, such as ethnicity, gender, or complexity, ensuring a uniform application of the title across a diverse set of names. This transformation could be indicative of a setting where the individuals' roles or achievements are being formally recognized, such as in academic publications, professional directories, or event programs where titles are customary., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    Transforms the given name by retaining the first name and prefixing it with 'Dr.'.

    Parameters:
    name (str): A string containing the first name followed by the last name.

    Returns:
    str: A string with the first name prefixed with 'Dr.'.
    """
    # Split the input name into first and last names
    first_name = name.split()[0]
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

# End time: 2024-04-09 19:24:33.599388
# Elapsed time in seconds: 6.459979373001261


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

