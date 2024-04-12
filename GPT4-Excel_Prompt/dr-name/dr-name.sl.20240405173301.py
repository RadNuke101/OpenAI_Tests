# Start time: 2024-04-05 17:45:45.853817

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    # Split the name by spaces to isolate the first name
    first_name = name.split()[0]
    # Return the formatted string with "Dr." prefix and the first name
    return "Dr. " + first_name

# Test cases
generated_function('Nancy FreeHafer')
generated_function('Andrew Cencici')
generated_function('Jan Kotas')
generated_function('Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-05 17:45:48.436491
# Elapsed time in seconds: 2.582610344999921