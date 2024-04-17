# Start time: 2024-04-10 15:33:33.840071

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of pairs of first names and last names.
- The first names in the input data include Launa, Lakenya, Brendan, Bradford, Rudolf, and Lara.
- The last names in the input data include Withers, Edison, Hage, Lango, Akiyama, and Constable.

Summary for Output Column Data:
- The output column data consists of the last names followed by the first names from the input data.
- The output column includes Withers Launa, Edison Lakenya, Hage Brendan, Lango Bradford, Akiyama Rudolf, and Constable Lara.

Relationship between Input and Output:
- The relationship between the input and output is that the last names from the input data are followed by the first names in the output data.
- The output column data is a rearrangement of the input data, with the last names coming before the first names.
- This relationship is consistent across all input-output pairs provided., and input as ['Launa', 'Withers'] output is Withers Launa, input as ['Lakenya', 'Edison'] output is Edison Lakenya, input as ['Brendan', 'Hage'] output is Hage Brendan, input as ['Bradford', 'Lango'] output is Lango Bradford, input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(first_name, last_name):
    # Concatenate the last name followed by the first name
    output = last_name + ' ' + first_name
    return output

# Test cases
print(generated_function('Launa', 'Withers'))
print(generated_function('Lakenya', 'Edison'))
print(generated_function('Brendan', 'Hage'))
print(generated_function('Bradford', 'Lango'))
print(generated_function('Rudolf', 'Akiyama'))
print(generated_function('Lara', 'Constable'))
print(generated_function("Launa", "Withers"))  ## Output: Withers Launa
print(generated_function("Lakenya", "Edison"))  ## Output: Edison Lakenya
print(generated_function("Brendan", "Hage"))  ## Output: Hage Brendan
print(generated_function("Bradford", "Lango"))  ## Output: Lango Bradford
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama Rudolf
print(generated_function("Lara", "Constable"))  ## Output: Constable Lara

# End time: 2024-04-10 15:33:36.198976
# Elapsed time in seconds: 2.3588531750001493