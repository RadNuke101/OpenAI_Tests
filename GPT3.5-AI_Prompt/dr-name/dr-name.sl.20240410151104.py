# Start time: 2024-04-10 15:19:08.721577

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of names of individuals, with titles such as Nancy FreeHafer, Andrew Cencici, Jan Kotas, and Mariya Sergienko.

Summary for Output Column Data:
- The output column data consists of titles such as Dr. Nancy, Dr. Andrew, Dr. Jan, and Dr. Mariya.

Relationship between Input and Output:
- The relationship between the input and output is that the input column data contains full names of individuals, while the output column data includes the title "Dr." followed by the first name of the individual. It appears that the output is generated by adding the title "Dr." to the first name of each individual in the input data., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name and last name
    first_name = input_str.split()[0]
    
    # Add the title "Dr." to the first name
    output = "Dr. " + first_name
    
    return output

# Test cases
print(generated_function('Nancy FreeHafer')) # Dr. Nancy
print(generated_function('Andrew Cencici')) # Dr. Andrew
print(generated_function('Jan Kotas')) # Dr. Jan
print(generated_function('Mariya Sergienko')) # Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 15:19:10.808441
# Elapsed time in seconds: 2.0872224110003117