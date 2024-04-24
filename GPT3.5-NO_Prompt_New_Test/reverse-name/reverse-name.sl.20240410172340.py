# Start time: 2024-04-10 17:34:00.735468

'''
Prompt:
Given that input as ['Launa', 'Withers'] output is Withers Launa, input as ['Lakenya', 'Edison'] output is Edison Lakenya, input as ['Brendan', 'Hage'] output is Hage Brendan, input as ['Bradford', 'Lango'] output is Lango Bradford, input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        first_name = input_list[0].strip()
        last_name = input_list[1].strip()
        return last_name + ' ' + first_name
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(generated_function('Launa, Withers'))
print(generated_function('Lakenya, Edison'))
print(generated_function('Brendan, Hage'))
print(generated_function('Bradford, Lango'))
print(generated_function('Rudolf, Akiyama'))
print(generated_function('Lara, Constable'))
print(generated_function("Launa", "Withers"))  ## Output: Withers Launa
print(generated_function("Lakenya", "Edison"))  ## Output: Edison Lakenya
print(generated_function("Brendan", "Hage"))  ## Output: Hage Brendan
print(generated_function("Bradford", "Lango"))  ## Output: Lango Bradford
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama Rudolf
print(generated_function("Lara", "Constable"))  ## Output: Constable Lara

# End time: 2024-04-10 17:34:02.991418
# Elapsed time in seconds: 2.2559224560000075


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: Withers Launa
print(generated_function("Lakenya", "Edison"))  ## Output: Edison Lakenya
print(generated_function("Brendan", "Hage"))  ## Output: Hage Brendan
print(generated_function("Bradford", "Lango"))  ## Output: Lango Bradford
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama Rudolf
print(generated_function("Lara", "Constable"))  ## Output: Constable Lara


print(generated_function("Wyatt", "Davis"))  ### Output: Davis Wyatt
print(generated_function("Aiden", "Clark"))  ### Output: Clark Aiden
print(generated_function("Chloe", "Adams"))  ### Output: Adams Chloe
print(generated_function("Sophia", "Coleman"))  ### Output: Coleman Sophia
print(generated_function("Mason", "Thompson"))  ### Output: Thompson Mason
print(generated_function("Ava", "Bennett"))  ### Output: Bennett Ava
print(generated_function("Carter", "Edwards"))  ### Output: Edwards Carter
print(generated_function("Emma", "Reynolds"))  ### Output: Reynolds Emma
print(generated_function("Elijah", "Foster"))  ### Output: Foster Elijah
print(generated_function("Olivia", "Parker"))  ### Output: Parker Olivia
print(generated_function("Nolan", "Cooper"))  ### Output: Cooper Nolan
print(generated_function("Gabriel", "Hayes"))  ### Output: Hayes Gabriel
print(generated_function("Caleb", "Johnson"))  ### Output: Johnson Caleb
print(generated_function("Benjamin", "Hayes"))  ### Output: Hayes Benjamin
print(generated_function("Owen", "Morgan"))  ### Output: Morgan Owen
print(generated_function("Caleb", "Mitchell"))  ### Output: Mitchell Caleb
print(generated_function("Harper", "Taylor"))  ### Output: Taylor Harper
print(generated_function("Amelia", "Nelson"))  ### Output: Nelson Amelia
print(generated_function("Grace", "Harrison"))  ### Output: Harrison Grace
print(generated_function("Logan", "Smith"))  ### Output: Smith Logan
print(generated_function("Abigail", "Cooper"))  ### Output: Cooper Abigail
print(generated_function("Zoey", "Turner"))  ### Output: Turner Zoey
print(generated_function("Madison", "Foster"))  ### Output: Foster Madison
print(generated_function("Scarlett", "Walker"))  ### Output: Walker Scarlett
print(generated_function("Jackson", "Turner"))  ### Output: Turner Jackson
print(generated_function("Samuel", "Wright"))  ### Output: Wright Samuel
print(generated_function("Isabella", "Brooks"))  ### Output: Brooks Isabella
print(generated_function("Liam", "Carter"))  ### Output: Carter Liam
print(generated_function("Lily", "Anderson"))  ### Output: Anderson Lily

# TEST SCRIPTS APPENDED!

