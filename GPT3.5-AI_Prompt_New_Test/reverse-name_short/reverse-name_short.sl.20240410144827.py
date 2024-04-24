# Start time: 2024-04-10 14:56:00.248055

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (First Names):
- The first names in the input column are Launa, Lakenya, Brendan, Bradford, Rudolf, Lara.
- The names appear to be of different origins and do not follow a specific pattern.

Summary for Input Column 2 (Last Names):
- The last names in the input column are Withers, Edison, Hage, Lango, Akiyama, Constable.
- Similar to the first names, the last names also seem to be diverse and do not have a common theme.

Summary for Output Column (Last Name First, First Name Last):
- The output column follows a consistent pattern of displaying the last name first followed by the first name.
- This format is maintained across all the input data provided.

Relationship between Input and Output:
- The output column consistently displays the last name first followed by the first name, regardless of the input data.
- There does not seem to be a direct relationship between the input first names and last names that determines the order in the output.
- The output format appears to be a fixed rule applied to all input data, rather than being influenced by the specific input names., and input as ['Launa', 'Withers'] output is Withers Launa, input as ['Lakenya', 'Edison'] output is Edison Lakenya, input as ['Brendan', 'Hage'] output is Hage Brendan, input as ['Bradford', 'Lango'] output is Lango Bradford, input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    # Concatenate the last name first followed by the first name
    output = last_name + " " + first_name
    return output

# Test cases
print(generated_function('Launa', 'Withers'))
print(generated_function('Lakenya', 'Edison'))
print(generated_function('Brendan', 'Hage'))
print(generated_function('Bradford', 'Lango'))
print(generated_function('Rudolf', 'Akiyama'))
print(generated_function('Lara', 'Constable'))
print(generated_function("Launa", "Withers"))  ## Output: Withers Launa
print(generated_function("Lakenya", "Edison"))  ## Output: Edison Lakenya
print(generated_function("Brendan", "Hage"))  ## Output: Hage Brendan
print(generated_function("Bradford", "Lango"))  ## Output: Lango Bradford
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama Rudolf
print(generated_function("Lara", "Constable"))  ## Output: Constable Lara

# End time: 2024-04-10 14:56:02.525222
# Elapsed time in seconds: 2.277112838999983


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: Withers Launa
print(generated_function("Lakenya", "Edison"))  ## Output: Edison Lakenya
print(generated_function("Brendan", "Hage"))  ## Output: Hage Brendan
print(generated_function("Bradford", "Lango"))  ## Output: Lango Bradford
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama Rudolf
print(generated_function("Lara", "Constable"))  ## Output: Constable Lara


print(generated_function("Madison", "Foster"))  ### Output: Foster Madison
print(generated_function("Caleb", "Mitchell"))  ### Output: Mitchell Caleb
print(generated_function("Aiden", "Clark"))  ### Output: Clark Aiden
print(generated_function("Owen", "Morgan"))  ### Output: Morgan Owen
print(generated_function("Mason", "Thompson"))  ### Output: Thompson Mason
print(generated_function("Sophia", "Coleman"))  ### Output: Coleman Sophia
print(generated_function("Zoey", "Turner"))  ### Output: Turner Zoey
print(generated_function("Wyatt", "Davis"))  ### Output: Davis Wyatt
print(generated_function("Logan", "Smith"))  ### Output: Smith Logan
print(generated_function("Abigail", "Cooper"))  ### Output: Cooper Abigail
print(generated_function("Liam", "Carter"))  ### Output: Carter Liam
print(generated_function("Scarlett", "Walker"))  ### Output: Walker Scarlett
print(generated_function("Caleb", "Johnson"))  ### Output: Johnson Caleb
print(generated_function("Benjamin", "Hayes"))  ### Output: Hayes Benjamin
print(generated_function("Ava", "Bennett"))  ### Output: Bennett Ava
print(generated_function("Grace", "Harrison"))  ### Output: Harrison Grace
print(generated_function("Gabriel", "Hayes"))  ### Output: Hayes Gabriel
print(generated_function("Isabella", "Brooks"))  ### Output: Brooks Isabella
print(generated_function("Olivia", "Parker"))  ### Output: Parker Olivia
print(generated_function("Nolan", "Cooper"))  ### Output: Cooper Nolan
print(generated_function("Elijah", "Foster"))  ### Output: Foster Elijah
print(generated_function("Jackson", "Turner"))  ### Output: Turner Jackson
print(generated_function("Amelia", "Nelson"))  ### Output: Nelson Amelia
print(generated_function("Samuel", "Wright"))  ### Output: Wright Samuel
print(generated_function("Emma", "Reynolds"))  ### Output: Reynolds Emma
print(generated_function("Harper", "Taylor"))  ### Output: Taylor Harper
print(generated_function("Lily", "Anderson"))  ### Output: Anderson Lily
print(generated_function("Chloe", "Adams"))  ### Output: Adams Chloe
print(generated_function("Carter", "Edwards"))  ### Output: Edwards Carter

# TEST SCRIPTS APPENDED!

