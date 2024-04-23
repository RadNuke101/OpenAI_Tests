# Start time: 2024-04-09 17:36:49.540846

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each containing a series of first names and last names, respectively. The first names column includes a variety of names, such as Launa, Lakenya, Brendan, Bradford, and Rudolf, indicating a diverse set of names without any apparent pattern regarding origin, gender, or ethnicity. The last names column, including surnames like Withers, Edison, Hage, Lango, and Akiyama, also showcases a diversity in terms of origin and phonetic composition. The names in both columns are qualitative in nature, representing individual identities without any inherent numerical value or order.

### Output Column Summary:

The output data is a transformation of the input data, formatted in a specific way: it takes the last name from the input and appends the first initial of the first name, followed by a period. The format is "Lastname, F.," where "Lastname" is the surname from the input and "F" is the first letter of the given name. This output format is commonly used in formal contexts, such as academic publications, professional directories, or legal documents, to standardize the way names are presented. The output retains the qualitative nature of the input data but restructures it into a more formal and standardized representation.

### Relationship Summary:

The relationship between the input and output data is a process of transformation and standardization. The input data, consisting of full first and last names, is reorganized to produce a formalized naming convention in the output. This process involves selecting the last name from the input and appending the first initial of the first name, followed by a period. This transformation is consistent across all data points, indicating a rule-based approach to generating the output from the given input. The purpose of this transformation is likely to create a uniform format for presenting names, which can be particularly useful in contexts where space is limited or where a formal presentation of names is required. The process respects the qualitative nature of the data while applying a systematic method to reformat it according to specific conventions., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    """
    Transforms the input first and last names into a standardized format.
    
    Args:
    first_name (str): The first name of an individual.
    last_name (str): The last name of an individual.
    
    Returns:
    str: A string formatted as "Lastname, F.," where "Lastname" is the last name
         and "F" is the first initial of the first name followed by a period.
    """
    # Extract the first initial of the first name
    first_initial = first_name[0]
    # Format and return the output string
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

# End time: 2024-04-09 17:37:00.850093
# Elapsed time in seconds: 11.308935535002092


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

