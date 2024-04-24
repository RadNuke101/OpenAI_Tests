# Start time: 2024-04-05 17:08:16.143475

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the second word
    return phrase.split()[1]

# Test cases
generated_function('Nancy FreeHafer')
generated_function('Andrew Cencici')
generated_function('Jan Kotas')
generated_function('Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-05 17:08:18.093431
# Elapsed time in seconds: 1.949921248999999


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko


print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Scarlett Walker"))  ### Output: Walker
print(generated_function("Caleb Johnson"))  ### Output: Johnson
print(generated_function("Amelia Nelson"))  ### Output: Nelson
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Jackson Turner"))  ### Output: Turner
print(generated_function("Gabriel Hayes"))  ### Output: Hayes
print(generated_function("Isabella Brooks"))  ### Output: Brooks
print(generated_function("Zoey Turner"))  ### Output: Turner
print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Carter Edwards"))  ### Output: Edwards
print(generated_function("Madison Foster"))  ### Output: Foster
print(generated_function("Harper Taylor"))  ### Output: Taylor
print(generated_function("Ava Bennett"))  ### Output: Bennett
print(generated_function("Nolan Cooper"))  ### Output: Cooper
print(generated_function("Abigail Cooper"))  ### Output: Cooper
print(generated_function("Lily Anderson"))  ### Output: Anderson
print(generated_function("Hannah Martin"))  ### Output: Martin
print(generated_function("Owen Morgan"))  ### Output: Morgan
print(generated_function("Chloe Adams"))  ### Output: Adams
print(generated_function("Wyatt Davis"))  ### Output: Davis
print(generated_function("Elijah Foster"))  ### Output: Foster
print(generated_function("Sophia Coleman"))  ### Output: Coleman
print(generated_function("Samuel Wright"))  ### Output: Wright
print(generated_function("Logan Smith"))  ### Output: Smith
print(generated_function("Liam Carter"))  ### Output: Carter
print(generated_function("Mason Thompson"))  ### Output: Thompson
print(generated_function("Aiden Clark"))  ### Output: Clark
print(generated_function("Grace Harrison"))  ### Output: Harrison

# TEST SCRIPTS APPENDED!

