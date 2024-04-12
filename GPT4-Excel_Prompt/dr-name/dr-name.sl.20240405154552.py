# Start time: 2024-04-05 16:00:45.500475

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(name):
    """
    This function takes a full name as input and returns a string that prefixes 'Dr. ' to the first name.

    :param name: A string representing the full name of a person.
    :return: A string that prefixes 'Dr. ' to the first name of the person.
    """
    # Split the name by space to separate the first name from the rest
    first_name = name.split()[0]
    # Return the formatted string with 'Dr. ' prefix
    return "Dr. " + first_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Expected output: Dr. Nancy
print(generated_function('Andrew Cencici'))  # Expected output: Dr. Andrew
print(generated_function('Jan Kotas'))  # Expected output: Dr. Jan
print(generated_function('Mariya Sergienko'))  # Expected output: Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-05 16:00:52.048764
# Elapsed time in seconds: 6.548094959999958