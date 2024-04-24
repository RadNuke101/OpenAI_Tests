# Start time: 2024-04-10 16:09:16.085268

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (First Names):
- The first names in the input column data are diverse and unique, ranging from Launa to Rudolf.
- There is no apparent pattern or commonality among the first names.

Summary for Input Column 2 (Last Names):
- The last names in the input column data are also varied, including Withers, Edison, Hage, Lango, and Akiyama.
- Similar to the first names, there is no clear pattern or similarity among the last names.

Summary for Output Column (Formatted Names):
- The output column consists of formatted names in the format "Last Name, First Initial." For example, Withers, L. and Edison, L.
- The output column shows a consistent pattern of displaying last names followed by a comma and the first initial of the first name.

Relationship between Input and Output:
- The relationship between the input and output columns is that the last name from the input is placed first in the output, followed by a comma and the first initial of the first name.
- This relationship is consistent across all input data, indicating a systematic formatting process to generate the output.
- The output column serves as a standardized way of presenting the input data in a specific format, making it easier to identify individuals based on their last names and first initials., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(first_name, last_name):
    # Format the names as "Last Name, First Initial"
    formatted_name = last_name + ', ' + first_name[0] + '.'
    
    return formatted_name

# Test cases
print(generated_function('Launa', 'Withers'))
print(generated_function('Lakenya', 'Edison'))
print(generated_function('Brendan', 'Hage'))
print(generated_function('Bradford', 'Lango'))
print(generated_function('Rudolf', 'Akiyama'))
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.

# End time: 2024-04-10 16:09:17.808298
# Elapsed time in seconds: 1.7229935110008228


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

