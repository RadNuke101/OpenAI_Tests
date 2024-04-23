# Start time: 2024-04-09 19:19:04.600629

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column 1 Summary (First Names):
The first input column consists of a list of first names, which are diverse in origin and phonetics. These names include Launa, Lakenya, Brendan, Bradford, and Rudolf. The variety in the names suggests a multicultural dataset without a specific focus on any single region or ethnicity. The names range from more traditional and common ones to those that might be considered unique or less commonly heard. This diversity in first names does not directly influence the structure of the output but adds a qualitative richness to the dataset.

### Input Column 2 Summary (Last Names):
The second input column is a collection of last names: Withers, Edison, Hage, Lango, and Akiyama. Similar to the first names, these last names are varied in their origins, indicating a broad and inclusive dataset. The last names range from those of English origin to those that may be of Japanese origin (e.g., Akiyama), showcasing a global representation. This column is crucial as it directly contributes to the formation of the output, with each last name being retained in full.

### Output Column Summary:
The output column presents a transformation of the input data into a standardized format commonly used in bibliographies or formal listings. The format is "[Last Name], [First Initial].", which serves to anonymize the first name to an initial while keeping the last name intact. This transformation suggests a formal or academic use case, where such a format is often preferred for consistency and space-saving. The relationship between the input and output is direct, with the last name from the second input column being used in full and the first name from the first input column being reduced to its initial, followed by a period.

### Relationship Summary:
The transformation from the input columns to the output column demonstrates a process of standardization and anonymization of personal names. The first names are anonymized to their initials, reducing the personal information conveyed, while the last names are kept intact, ensuring that the identity is still recognizable to those familiar with the individual but in a more formal and concise manner. This process is common in environments where space is limited or where a uniform format for names is required, such as academic publications, official documents, and databases. The relationship between the input and output underscores the importance of maintaining a balance between personal identity and the need for standardization in certain contexts., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    Transforms first and last names into a standardized bibliographic format.
    
    Parameters:
    first_name (str): The first name of a person.
    last_name (str): The last name of a person.
    
    Returns:
    str: A string formatted as "[Last Name], [First Initial]."
    """
    # Extract the first initial from the first name
    first_initial = first_name[0]
    # Format and return the output as per the specified bibliographic format
    return f"{last_name}, {first_initial}."

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

# End time: 2024-04-09 19:19:11.583687
# Elapsed time in seconds: 6.982891119998385


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.


print(generated_function("Wyatt", "Davis"))  ### Output: Davis, W.
print(generated_function("Hannah", "Martin"))  ### Output: Martin, H.
print(generated_function("Mason", "Thompson"))  ### Output: Thompson, M.
print(generated_function("Isabella", "Brooks"))  ### Output: Brooks, I.
print(generated_function("Caleb", "Johnson"))  ### Output: Johnson, C.
print(generated_function("Caleb", "Mitchell"))  ### Output: Mitchell, C.
print(generated_function("Chloe", "Adams"))  ### Output: Adams, C.
print(generated_function("Benjamin", "Hayes"))  ### Output: Hayes, B.
print(generated_function("Zoey", "Turner"))  ### Output: Turner, Z.
print(generated_function("Lily", "Anderson"))  ### Output: Anderson, L.
print(generated_function("Grace", "Harrison"))  ### Output: Harrison, G.
print(generated_function("Harper", "Taylor"))  ### Output: Taylor, H.
print(generated_function("Scarlett", "Walker"))  ### Output: Walker, S.
print(generated_function("Amelia", "Nelson"))  ### Output: Nelson, A.
print(generated_function("Liam", "Carter"))  ### Output: Carter, L.
print(generated_function("Samuel", "Wright"))  ### Output: Wright, S.
print(generated_function("Owen", "Morgan"))  ### Output: Morgan, O.
print(generated_function("Gabriel", "Hayes"))  ### Output: Hayes, G.
print(generated_function("Logan", "Smith"))  ### Output: Smith, L.
print(generated_function("Madison", "Foster"))  ### Output: Foster, M.
print(generated_function("Carter", "Edwards"))  ### Output: Edwards, C.
print(generated_function("Jackson", "Turner"))  ### Output: Turner, J.
print(generated_function("Sophia", "Coleman"))  ### Output: Coleman, S.
print(generated_function("Emma", "Reynolds"))  ### Output: Reynolds, E.
print(generated_function("Aiden", "Clark"))  ### Output: Clark, A.
print(generated_function("Nolan", "Cooper"))  ### Output: Cooper, N.
print(generated_function("Elijah", "Foster"))  ### Output: Foster, E.
print(generated_function("Abigail", "Cooper"))  ### Output: Cooper, A.
print(generated_function("Ava", "Bennett"))  ### Output: Bennett, A.
print(generated_function("Olivia", "Parker"))  ### Output: Parker, O.

# TEST SCRIPTS APPENDED!

