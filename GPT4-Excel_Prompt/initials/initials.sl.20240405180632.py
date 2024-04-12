# Start time: 2024-04-05 18:14:06.127511

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period, and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the phrase into words
    words = phrase.split()
    # Initialize an empty string to store the initials
    initials = ""
    # Check if there are at least two words to extract initials from
    if len(words) >= 2:
        # Extract the first letter of the first word, add a period
        initials += words[0][0] + "."
        # Extract the first letter of the second word, add a period
        initials += words[1][0] + "."
    # Return the initials
    return initials

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: N.F.
print(generated_function('Andrew Cencici'))   # Expected output: A.C.
print(generated_function('Jan Kotas'))        # Expected output: J.K.
print(generated_function('Mariya Sergienko')) # Expected output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-05 18:14:11.007749
# Elapsed time in seconds: 4.880091179998999