# Start time: 2024-04-05 15:53:44.506373

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the first element
    return phrase.split()[0]

# Test cases
result1 = generated_function('Nancy FreeHafer')
result2 = generated_function('Andrew Cencici')
result3 = generated_function('Jan Kotas')
result4 = generated_function('Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-05 15:53:47.589203
# Elapsed time in seconds: 3.0827282230000037


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya


print(generated_function("Emma Reynolds"))  ### Output: Emma
print(generated_function("Jackson Turner"))  ### Output: Jackson
print(generated_function("Olivia Parker"))  ### Output: Olivia
print(generated_function("Lily Anderson"))  ### Output: Lily
print(generated_function("Grace Harrison"))  ### Output: Grace
print(generated_function("Benjamin Hayes"))  ### Output: Benjamin
print(generated_function("Mason Thompson"))  ### Output: Mason
print(generated_function("Caleb Mitchell"))  ### Output: Caleb
print(generated_function("Wyatt Davis"))  ### Output: Wyatt

# TEST SCRIPTS APPENDED!

