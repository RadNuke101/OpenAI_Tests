# Start time: 2024-04-09 15:46:26.933542

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Data Summary:

**First Names (Column 1):**
- The first names provided in the input data are diverse, covering a range of origins and phonetic styles. Names like Launa, Lakenya, Brendan, Bradford, Rudolf, and Lara indicate a variety of cultural backgrounds or preferences in naming conventions. 
- The first names all start with either 'L', 'B', or 'R', showing a limited alphabetical range in this particular dataset.
- The names vary in length and complexity, from short and simple (e.g., Lara) to longer and more complex (e.g., Lakenya).

**Last Names (Column 2):**
- The last names, such as Withers, Edison, Hage, Lango, Akiyama, and Constable, also display diversity, suggesting a range of ethnic or geographical origins. This variety indicates that the dataset encompasses a broad spectrum of backgrounds.
- Unlike the first names, the last names do not show a pattern in their initial letters, indicating a more random or varied selection.
- The last names vary in length but generally tend to be longer than the first names, adding a level of complexity and uniqueness to each entry.

### Output Column Data Summary:

**Formatted Names:**
- The output data presents a standardized format of initials followed by a period and the full last name (e.g., L. Withers, B. Hage). This format simplifies and unifies the presentation of names, making it easier to recognize and categorize individuals by their last names while still retaining a hint of their first name's uniqueness through the initial.
- This transformation emphasizes the last name over the first, which could be useful in contexts where surnames are more relevant, such as in formal listings, academic citations, or professional environments.
- The use of initials reduces the emphasis on the diversity and complexity of the first names, streamlining the data into a more uniform and concise format.

### Relationship Between Input and Output:

- The relationship between the input and output data is a transformation process that simplifies and standardizes the presentation of personal names. 
- This process retains essential identity markers (the initial of the first name and the full last name) while discarding the more detailed and diverse elements of the first names. 
- The transformation suggests a prioritization of surname recognition and a move towards a formal or professional naming convention, which could be particularly relevant in contexts where space is limited or where uniformity is desired for ease of sorting, searching, or referencing.
- The method of transformation is consistent across all entries, indicating a rule-based approach that could easily be applied to a larger dataset with similar diversity in names., and input as ['Launa', 'Withers'] output is L. Withers, input as ['Lakenya', 'Edison'] output is L. Edison, input as ['Brendan', 'Hage'] output is B. Hage, input as ['Bradford', 'Lango'] output is B. Lango, input as ['Rudolf', 'Akiyama'] output is R. Akiyama, input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a formatted string.
    The formatted string consists of the first initial of the first name, followed by a period and the full last name.
    
    Parameters:
    - first_name (str): The first name of a person.
    - last_name (str): The last name of a person.
    
    Returns:
    - str: A formatted string with the initial of the first name and the full last name.
    """
    # Extract the first letter of the first name, add a period, and concatenate the last name
    formatted_name = first_name[0] + ". " + last_name
    return formatted_name

# Test cases
print(generated_function('Launa', 'Withers'))  # Expected output: L. Withers
print(generated_function('Lakenya', 'Edison'))  # Expected output: L. Edison
print(generated_function('Brendan', 'Hage'))  # Expected output: B. Hage
print(generated_function('Bradford', 'Lango'))  # Expected output: B. Lango
print(generated_function('Rudolf', 'Akiyama'))  # Expected output: R. Akiyama
print(generated_function('Lara', 'Constable'))  # Expected output: L. Constable
print(generated_function("Launa", "Withers"))  ## Output: L. Withers
print(generated_function("Lakenya", "Edison"))  ## Output: L. Edison
print(generated_function("Brendan", "Hage"))  ## Output: B. Hage
print(generated_function("Bradford", "Lango"))  ## Output: B. Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: R. Akiyama
print(generated_function("Lara", "Constable"))  ## Output: L. Constable

# End time: 2024-04-09 15:46:40.844455
# Elapsed time in seconds: 13.9105262209996


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: L. Withers
print(generated_function("Lakenya", "Edison"))  ## Output: L. Edison
print(generated_function("Brendan", "Hage"))  ## Output: B. Hage
print(generated_function("Bradford", "Lango"))  ## Output: B. Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: R. Akiyama
print(generated_function("Lara", "Constable"))  ## Output: L. Constable


print(generated_function("Lily", "Anderson"))  ### Output: L. Anderson
print(generated_function("Chloe", "Adams"))  ### Output: C. Adams
print(generated_function("Grace", "Harrison"))  ### Output: G. Harrison
print(generated_function("Nolan", "Cooper"))  ### Output: N. Cooper
print(generated_function("Samuel", "Wright"))  ### Output: S. Wright
print(generated_function("Emma", "Reynolds"))  ### Output: E. Reynolds
print(generated_function("Ava", "Bennett"))  ### Output: A. Bennett
print(generated_function("Scarlett", "Walker"))  ### Output: S. Walker
print(generated_function("Caleb", "Johnson"))  ### Output: C. Johnson
print(generated_function("Liam", "Carter"))  ### Output: L. Carter
print(generated_function("Benjamin", "Hayes"))  ### Output: B. Hayes
print(generated_function("Wyatt", "Davis"))  ### Output: W. Davis
print(generated_function("Caleb", "Mitchell"))  ### Output: C. Mitchell
print(generated_function("Sophia", "Coleman"))  ### Output: S. Coleman
print(generated_function("Gabriel", "Hayes"))  ### Output: G. Hayes
print(generated_function("Jackson", "Turner"))  ### Output: J. Turner
print(generated_function("Elijah", "Foster"))  ### Output: E. Foster
print(generated_function("Aiden", "Clark"))  ### Output: A. Clark
print(generated_function("Isabella", "Brooks"))  ### Output: I. Brooks
print(generated_function("Carter", "Edwards"))  ### Output: C. Edwards
print(generated_function("Logan", "Smith"))  ### Output: L. Smith
print(generated_function("Harper", "Taylor"))  ### Output: H. Taylor
print(generated_function("Owen", "Morgan"))  ### Output: O. Morgan
print(generated_function("Mason", "Thompson"))  ### Output: M. Thompson
print(generated_function("Amelia", "Nelson"))  ### Output: A. Nelson
print(generated_function("Abigail", "Cooper"))  ### Output: A. Cooper
print(generated_function("Hannah", "Martin"))  ### Output: H. Martin
print(generated_function("Madison", "Foster"))  ### Output: M. Foster
print(generated_function("Olivia", "Parker"))  ### Output: O. Parker
print(generated_function("Zoey", "Turner"))  ### Output: Z. Turner

# TEST SCRIPTS APPENDED!

