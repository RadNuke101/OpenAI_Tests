# Start time: 2024-04-05 16:51:04.024032

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a space, and then the the first letter of the second input, followed by a period, and input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    # Return the formatted string as per the prompt
    return f"{first_name} {last_name[0]}."

# Test cases
print(generated_function('Nancy', 'FreeHafer'))
print(generated_function('Andrew', 'Cencici'))
print(generated_function('Jan', 'Kotas'))
print(generated_function('Mariya', 'Sergienko'))
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-05 16:51:06.759668
# Elapsed time in seconds: 2.735603402000379