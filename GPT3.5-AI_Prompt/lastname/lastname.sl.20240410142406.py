# Start time: 2024-04-10 14:36:09.506499

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each entry in the input column data is a combination of a first name and a last name.
- The last names in the input column data vary in length and structure.

Summary for Output Column Data:
- The output column data consists of last names extracted from the input column data.
- Each entry in the output column data represents the last name of the corresponding individual in the input column data.
- The last names in the output column data vary in length and structure.

Relationship between Input and Output:
- The output column data is derived from the last names present in the input column data.
- The output column data serves as a simplified representation of the last names in the input column data.
- By extracting and summarizing the last names, the output column data provides a concise overview of the diverse range of last names present in the input column data., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the output
    output = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input into first name and last name
        names = arg.split()
        last_name = names[-1]  # Extract the last name
        output.append(last_name)  # Add the last name to the output list
    
    return output

# Test cases
generated_function('Nancy FreeHafer', 'Andrew Cencici', 'Jan Kotas', 'Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-10 14:36:11.505985
# Elapsed time in seconds: 1.9994411479999599