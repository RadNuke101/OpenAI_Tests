# Start time: 2024-04-09 15:21:59.397843

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column 1 Summary (First Names):
The first input column consists of a diverse set of first names, each unique and representing a wide range of cultural backgrounds. These names include Launa, Lakenya, Brendan, Bradford, and Rudolf. The variety in the names suggests a multicultural dataset without any apparent bias towards a specific gender, ethnicity, or origin. The names vary in length and complexity, indicating a random selection without preference for simplicity or complexity in naming conventions.

### Input Column 2 Summary (Last Names):
The second input column contains last names that are equally diverse, including Withers, Edison, Hage, Lango, and Akiyama. Similar to the first names, these last names represent a broad spectrum of cultural backgrounds, suggesting an inclusive dataset. The last names vary in their phonetic and structural composition, indicating no specific pattern or preference in the selection process. This diversity in last names, like the first names, points to a dataset that values representation from various cultures and heritages.

### Output Column Summary:
The output column combines elements from both input columns but follows a specific format: it presents the last name followed by a comma, a space, and then the first initial of the given first name, ending with a period. For example, "Launa Withers" becomes "Withers, L." This transformation standardizes the way names are presented, making them uniform regardless of their origin or complexity. The output format is commonly used in formal and academic settings, suggesting that the purpose of this transformation might be to prepare the names for use in environments where such a format is required or preferred.

### Relationship Summary:
The relationship between the input columns and the output column is a process of standardization and simplification of names. The transformation takes diverse and culturally rich first and last names and converts them into a uniform format that emphasizes the last name followed by the initial of the first name. This process reduces the complexity and variety of the input names to a simple, widely recognized format. The purpose behind this could be to facilitate easier identification, sorting, or referencing of individuals in databases, publications, or formal documents where space is limited, and consistency is key. The transformation respects the individuality of each name by retaining the last name in full, which often carries significant cultural and familial importance, while simplifying the first name to an initial, thus balancing uniqueness with uniformity., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    This function takes a first name and a last name as inputs and returns a string
    that combines the last name, a comma, a space, and the first initial of the first name with a period.
    
    Parameters:
    first_name (str): The first name of a person.
    last_name (str): The last name of a person.
    
    Returns:
    str: A string formatted as 'Last Name, F.' where F is the first initial of the first name.
    """
    # Extract the first initial of the first name
    first_initial = first_name[0]
    # Combine the last name, a comma, a space, the first initial, and a period
    formatted_name = f"{last_name}, {first_initial}."
    return formatted_name

# Test cases
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

# End time: 2024-04-09 15:22:10.868533
# Elapsed time in seconds: 11.470500164999976


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

