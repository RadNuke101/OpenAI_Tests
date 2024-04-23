# Start time: 2024-04-09 21:24:29.526822

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each containing qualitative, personal information. The first column includes first names, while the second column contains last names. The names span a variety of cultural backgrounds, indicating a diverse dataset. The first names are single words, and the last names are also single words, suggesting a standard format for personal names in Western contexts. The data appears to be individual identifiers, likely representing different people. The names do not repeat, implying that each row represents a unique individual.

### Output Column Summary:

The output data is a single column that combines elements from both input columns into a new format. This format includes the full first name from the first input column and the initial (the first letter) of the last name from the second input column, followed by a period. The output maintains the individual identity from the input while abbreviating the last name, likely for purposes of brevity or privacy. The output is also qualitative, representing a concise version of the person's name.

### Relationship Between Input and Output:

The relationship between the input columns and the output column is a transformational one, where the output is derived by concatenating the first name (unchanged) from the first input column with the initial of the last name from the second input column, followed by a period. This process suggests a standard method of generating abbreviated names, possibly for use in contexts where full last names are unnecessary or where space or privacy concerns predominate. The transformation maintains the uniqueness and recognizability of each individual's name while offering a more compact or less formal representation. This method of name abbreviation is common in many professional and academic settings, providing a balance between personal identification and brevity., and input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that combines the first name with the initial of the last name followed by a period.
    
    Parameters:
    - first_name (str): The first name of the individual.
    - last_name (str): The last name of the individual.
    
    Returns:
    - str: A string that combines the first name with the initial of the last name followed by a period.
    """
    # Concatenate the first name with the initial of the last name followed by a period
    output = first_name + " " + last_name[0] + "."
    return output

# Test cases
print(generated_function('Nancy', 'FreeHafer'))  # Expected output: Nancy F.
print(generated_function('Andrew', 'Cencici'))  # Expected output: Andrew C.
print(generated_function('Jan', 'Kotas'))       # Expected output: Jan K.
print(generated_function('Mariya', 'Sergienko')) # Expected output: Mariya S.
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-09 21:24:39.868388
# Elapsed time in seconds: 10.341277958003047


# APPEND TEST SCRIPTS...
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.


print(generated_function("Ava", "Bennett"))  ### Output: Ava B.
print(generated_function("Owen", "Morgan"))  ### Output: Owen M.
print(generated_function("Hannah", "Martin"))  ### Output: Hannah M.
print(generated_function("Olivia", "Parker"))  ### Output: Olivia P.
print(generated_function("Mason", "Thompson"))  ### Output: Mason T.
print(generated_function("Logan", "Smith"))  ### Output: Logan S.
print(generated_function("Caleb", "Johnson"))  ### Output: Caleb J.
print(generated_function("Elijah", "Foster"))  ### Output: Elijah F.
print(generated_function("Grace", "Harrison"))  ### Output: Grace H.
print(generated_function("Jackson", "Turner"))  ### Output: Jackson T.
print(generated_function("Benjamin", "Hayes"))  ### Output: Benjamin H.
print(generated_function("Harper", "Taylor"))  ### Output: Harper T.
print(generated_function("Emma", "Reynolds"))  ### Output: Emma R.
print(generated_function("Wyatt", "Davis"))  ### Output: Wyatt D.
print(generated_function("Liam", "Carter"))  ### Output: Liam C.
print(generated_function("Chloe", "Adams"))  ### Output: Chloe A.
print(generated_function("Isabella", "Brooks"))  ### Output: Isabella B.
print(generated_function("Caleb", "Mitchell"))  ### Output: Caleb M.
print(generated_function("Aiden", "Clark"))  ### Output: Aiden C.
print(generated_function("Samuel", "Wright"))  ### Output: Samuel W.
print(generated_function("Amelia", "Nelson"))  ### Output: Amelia N.
print(generated_function("Lily", "Anderson"))  ### Output: Lily A.
print(generated_function("Gabriel", "Hayes"))  ### Output: Gabriel H.
print(generated_function("Scarlett", "Walker"))  ### Output: Scarlett W.
print(generated_function("Sophia", "Coleman"))  ### Output: Sophia C.
print(generated_function("Carter", "Edwards"))  ### Output: Carter E.
print(generated_function("Zoey", "Turner"))  ### Output: Zoey T.
print(generated_function("Madison", "Foster"))  ### Output: Madison F.
print(generated_function("Nolan", "Cooper"))  ### Output: Nolan C.
print(generated_function("Abigail", "Cooper"))  ### Output: Abigail C.

# TEST SCRIPTS APPENDED!

