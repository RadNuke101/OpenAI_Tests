# Start time: 2024-04-09 17:15:46.083999

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

#### First Name Column:
The first name column consists of a diverse set of given names, each unique and reflecting a variety of cultural backgrounds or naming conventions. The names included are Launa, Lakenya, Brendan, Bradford, and Rudolf. These names do not follow a specific pattern in terms of origin, length, or starting letter, indicating a broad and inclusive selection of individuals without a preference for any particular naming tradition.

#### Last Name Column:
The last name column also showcases a variety of surnames, including Withers, Edison, Hage, Lango, and Akiyama. Similar to the first names, these surnames represent a range of cultural backgrounds, suggesting a diverse group of individuals. There is no apparent pattern in terms of the origin or the alphabetical arrangement of these surnames, further emphasizing the diversity present in the dataset.

### Summary of Output Column Data:

The output format consistently transforms the input data into a standardized form, displaying the last name followed by a comma, a space, and the first initial of the given name with a period. This transformation suggests a formal or professional context where such a naming convention might be preferred, such as in academic citations, professional directories, or formal communication. The output uniformly applies this format across all entries, regardless of the cultural origin or the length of the names, ensuring a consistent and easily recognizable pattern for identifying individuals by their surname and the initial of their first name.

### Relationship Between Input and Output:

The relationship between the input and output data demonstrates a process of standardization and formalization of personal names. By converting full names into a format that prioritizes the surname followed by the initial of the first name, the output simplifies and unifies the way individuals are referred to, potentially making it easier to organize, search, and reference in contexts where uniformity and brevity are valued. This transformation respects the individuality of each name by retaining the unique surnames and the initials of the given names, while also adapting them into a format that is commonly used in formal and professional environments., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that formats the last name followed by a comma, a space, and the first initial
    of the given name with a period, which is a common format in formal or professional contexts.
    """
    # Extract the first initial of the given name
    first_initial = first_name[0]
    # Format the output as "Last Name, First Initial."
    formatted_output = f"{last_name}, {first_initial}."
    return formatted_output

# Test cases based on the provided input and expected output
print(generated_function('Launa', 'Withers'))  # Expected output: Withers, L.
print(generated_function('Lakenya', 'Edison'))  # Expected output: Edison, L.
print(generated_function('Brendan', 'Hage'))  # Expected output: Hage, B.
print(generated_function('Bradford', 'Lango'))  # Expected output: Lango, B.
print(generated_function('Rudolf', 'Akiyama'))  # Expected output: Akiyama, R.
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.

# End time: 2024-04-09 17:15:53.877451
# Elapsed time in seconds: 7.7933096650012885


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.


print(generated_function("Olivia", "Parker"))  ### Output: Parker, O.
print(generated_function("Harper", "Taylor"))  ### Output: Taylor, H.
print(generated_function("Ava", "Bennett"))  ### Output: Bennett, A.
print(generated_function("Samuel", "Wright"))  ### Output: Wright, S.
print(generated_function("Scarlett", "Walker"))  ### Output: Walker, S.
print(generated_function("Nolan", "Cooper"))  ### Output: Cooper, N.
print(generated_function("Carter", "Edwards"))  ### Output: Edwards, C.
print(generated_function("Amelia", "Nelson"))  ### Output: Nelson, A.
print(generated_function("Lily", "Anderson"))  ### Output: Anderson, L.
print(generated_function("Caleb", "Mitchell"))  ### Output: Mitchell, C.
print(generated_function("Benjamin", "Hayes"))  ### Output: Hayes, B.
print(generated_function("Mason", "Thompson"))  ### Output: Thompson, M.
print(generated_function("Aiden", "Clark"))  ### Output: Clark, A.
print(generated_function("Wyatt", "Davis"))  ### Output: Davis, W.
print(generated_function("Elijah", "Foster"))  ### Output: Foster, E.
print(generated_function("Emma", "Reynolds"))  ### Output: Reynolds, E.
print(generated_function("Isabella", "Brooks"))  ### Output: Brooks, I.
print(generated_function("Liam", "Carter"))  ### Output: Carter, L.
print(generated_function("Abigail", "Cooper"))  ### Output: Cooper, A.
print(generated_function("Logan", "Smith"))  ### Output: Smith, L.
print(generated_function("Chloe", "Adams"))  ### Output: Adams, C.
print(generated_function("Zoey", "Turner"))  ### Output: Turner, Z.
print(generated_function("Gabriel", "Hayes"))  ### Output: Hayes, G.
print(generated_function("Hannah", "Martin"))  ### Output: Martin, H.
print(generated_function("Sophia", "Coleman"))  ### Output: Coleman, S.
print(generated_function("Madison", "Foster"))  ### Output: Foster, M.
print(generated_function("Grace", "Harrison"))  ### Output: Harrison, G.
print(generated_function("Owen", "Morgan"))  ### Output: Morgan, O.
print(generated_function("Caleb", "Johnson"))  ### Output: Johnson, C.
print(generated_function("Jackson", "Turner"))  ### Output: Turner, J.

# TEST SCRIPTS APPENDED!

