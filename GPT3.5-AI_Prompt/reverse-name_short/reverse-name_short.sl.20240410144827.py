# Start time: 2024-04-10 14:56:00.248055

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (First Names):
- The first names in the input column are Launa, Lakenya, Brendan, Bradford, Rudolf, Lara.
- The names appear to be of different origins and do not follow a specific pattern.

Summary for Input Column 2 (Last Names):
- The last names in the input column are Withers, Edison, Hage, Lango, Akiyama, Constable.
- Similar to the first names, the last names also seem to be diverse and do not have a common theme.

Summary for Output Column (Last Name First, First Name Last):
- The output column follows a consistent pattern of displaying the last name first followed by the first name.
- This format is maintained across all the input data provided.

Relationship between Input and Output:
- The output column consistently displays the last name first followed by the first name, regardless of the input data.
- There does not seem to be a direct relationship between the input first names and last names that determines the order in the output.
- The output format appears to be a fixed rule applied to all input data, rather than being influenced by the specific input names., and input as ['Launa', 'Withers'] output is Withers Launa, input as ['Lakenya', 'Edison'] output is Edison Lakenya, input as ['Brendan', 'Hage'] output is Hage Brendan, input as ['Bradford', 'Lango'] output is Lango Bradford, input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    # Concatenate the last name first followed by the first name
    output = last_name + " " + first_name
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

# End time: 2024-04-10 14:56:02.525222
# Elapsed time in seconds: 2.277112838999983