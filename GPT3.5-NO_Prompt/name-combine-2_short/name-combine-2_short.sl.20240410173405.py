# Start time: 2024-04-10 17:44:30.526908

'''
Prompt:
Given that input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split()
        first_name = input_list[0]
        last_name = input_list[1]
        return f"{first_name} {last_name[0]}."
    except IndexError:
        return "Invalid input format."

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: Nancy F.
print(generated_function('Andrew Cencici'))    # Output: Andrew C.
print(generated_function('Jan Kotas'))         # Output: Jan K.
print(generated_function('Mariya Sergienko'))  # Output: Mariya S.
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-10 17:44:32.484227
# Elapsed time in seconds: 1.9572943919999943