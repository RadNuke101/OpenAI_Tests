# Start time: 2024-04-09 17:44:11.510898

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each representing a different type of qualitative information about individuals. The first column contains first names, while the second column includes last names. These names are diverse, indicating a variety of cultural backgrounds. The first names provided are "Nancy," "Andrew," "Jan," and "Mariya," showcasing a mix of gender and potentially cultural origins. The last names "FreeHafer," "Cencici," "Kotas," and "Sergienko" further indicate a variety of ethnic backgrounds. The data in these columns is nominal, meaning it categorizes individuals without implying any order or hierarchy.

### Output Column Summary:

The output data combines elements from both input columns into a single string per individual, following a specific format: the first name is kept intact, and the last name is abbreviated to its initial followed by a period ("."). This format provides a concise way to reference individuals, maintaining clarity on their identity while abbreviating the last name for brevity or privacy. The output retains the personal and cultural identity conveyed by the full names in the input while adapting it into a more formal or semi-anonymous form.

### Relationship Between Input and Output:

The transformation from the input columns to the output column demonstrates a process of data simplification and standardization. This process takes detailed personal information (full first and last names) and converts it into a standardized format that is easier to manage, communicate, or display in contexts where space is limited or where full last names are not necessary. The relationship between the input and output highlights a common practice in data handling where detailed information is condensed into a more manageable form without losing the essence of the original data. This method respects the individuality of the names (and by extension, the individuals they represent) while adapting to practical constraints or preferences for data presentation., and input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that combines the first name with the initial of the last name followed by a period.
    
    Parameters:
    - first_name (str): The first name of an individual.
    - last_name (str): The last name of an individual.
    
    Returns:
    - str: A string combining the first name and the initial of the last name followed by a period.
    """
    # Concatenate the first name with the initial of the last name followed by a period
    output = first_name + " " + last_name[0] + "."
    return output

# Test cases
print(generated_function('Nancy', 'FreeHafer'))  # Expected output: Nancy F.
print(generated_function('Andrew', 'Cencici'))   # Expected output: Andrew C.
print(generated_function('Jan', 'Kotas'))        # Expected output: Jan K.
print(generated_function('Mariya', 'Sergienko')) # Expected output: Mariya S.
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-09 17:44:19.623918
# Elapsed time in seconds: 8.112794626998948


# APPEND TEST SCRIPTS...
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.


print(generated_function("Jackson", "Turner"))  ### Output: Jackson T.
print(generated_function("Caleb", "Mitchell"))  ### Output: Caleb M.
print(generated_function("Olivia", "Parker"))  ### Output: Olivia P.
print(generated_function("Logan", "Smith"))  ### Output: Logan S.
print(generated_function("Sophia", "Coleman"))  ### Output: Sophia C.
print(generated_function("Amelia", "Nelson"))  ### Output: Amelia N.
print(generated_function("Isabella", "Brooks"))  ### Output: Isabella B.
print(generated_function("Zoey", "Turner"))  ### Output: Zoey T.
print(generated_function("Carter", "Edwards"))  ### Output: Carter E.
print(generated_function("Madison", "Foster"))  ### Output: Madison F.
print(generated_function("Owen", "Morgan"))  ### Output: Owen M.
print(generated_function("Elijah", "Foster"))  ### Output: Elijah F.
print(generated_function("Lily", "Anderson"))  ### Output: Lily A.
print(generated_function("Wyatt", "Davis"))  ### Output: Wyatt D.
print(generated_function("Harper", "Taylor"))  ### Output: Harper T.
print(generated_function("Ava", "Bennett"))  ### Output: Ava B.
print(generated_function("Nolan", "Cooper"))  ### Output: Nolan C.
print(generated_function("Chloe", "Adams"))  ### Output: Chloe A.
print(generated_function("Gabriel", "Hayes"))  ### Output: Gabriel H.
print(generated_function("Hannah", "Martin"))  ### Output: Hannah M.
print(generated_function("Abigail", "Cooper"))  ### Output: Abigail C.
print(generated_function("Mason", "Thompson"))  ### Output: Mason T.
print(generated_function("Caleb", "Johnson"))  ### Output: Caleb J.
print(generated_function("Samuel", "Wright"))  ### Output: Samuel W.
print(generated_function("Emma", "Reynolds"))  ### Output: Emma R.
print(generated_function("Liam", "Carter"))  ### Output: Liam C.
print(generated_function("Scarlett", "Walker"))  ### Output: Scarlett W.
print(generated_function("Aiden", "Clark"))  ### Output: Aiden C.
print(generated_function("Grace", "Harrison"))  ### Output: Grace H.
print(generated_function("Benjamin", "Hayes"))  ### Output: Benjamin H.

# TEST SCRIPTS APPENDED!

