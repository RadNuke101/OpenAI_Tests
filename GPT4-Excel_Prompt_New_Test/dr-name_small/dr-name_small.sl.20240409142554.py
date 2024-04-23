# Start time: 2024-04-09 15:54:17.880896

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing full names of individuals. Each entry in the column is a string that includes a first name followed by a last name, separated by a space. The names appear to be of diverse origins, indicating a variety of cultural backgrounds. The data does not include any titles, degrees, or professional designations attached to the names. The format is consistent across the dataset, with each entry adhering to the "FirstName LastName" structure. This consistency suggests that the data has been pre-processed or formatted to maintain uniformity. The names provided do not indicate gender, age, or any other demographic information beyond the possible cultural or ethnic origins suggested by the names themselves.

### Output Column Summary:

The output data, corresponding to the input column, transforms each full name into a format that includes a professional or academic title, specifically "Dr.", followed by the first name of the individual. The last name is omitted in the output. This transformation standardizes the output by applying the same title to all individuals, regardless of their original name's structure or cultural background. The use of "Dr." as a prefix suggests a context where the individuals are being recognized or addressed with a level of respect or authority, typically associated with academic, medical, or scientific professions. The output maintains the first name of each individual from the input, ensuring a personalized yet formal mode of address. The uniform application of the title "Dr." to all names, regardless of the diversity in the input, indicates an intention to elevate or formalize the status of each individual in the context of the dataset.

### Relationship Between Input and Output:

The transformation from the input to the output column demonstrates a process of formalization and professionalization of individual names by appending a common title, "Dr.", to the first name of each person. This process selectively retains the first name while discarding the last name, focusing on personal identification rather than familial or cultural lineage. The relationship between the input and output data underscores an intention to standardize the way individuals are addressed, possibly for the purposes of a specific professional, academic, or formal setting where such titles are relevant. The consistent application of the title "Dr." across a diverse set of names highlights a unifying approach to recognizing or honoring the individuals, suggesting that the context or environment values academic or professional achievements universally. This transformation does not alter the cultural diversity present in the first names but does place all individuals on an equal footing by bestowing upon them a common title of respect and authority., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    """
    Transforms a full name into a format that includes a professional or academic title "Dr.",
    followed by the first name of the individual. The last name is omitted in the output.
    
    Parameters:
    full_name (str): A string containing the first name and last name of an individual, separated by a space.
    
    Returns:
    str: A string that includes the title "Dr." followed by the first name of the individual.
    """
    # Split the full name into first name and last name
    first_name, _ = full_name.split()
    # Format and return the output
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

# End time: 2024-04-09 15:54:28.214793
# Elapsed time in seconds: 10.333610787998623


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

