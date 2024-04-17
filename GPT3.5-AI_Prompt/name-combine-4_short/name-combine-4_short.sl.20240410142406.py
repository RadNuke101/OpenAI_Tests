# Start time: 2024-04-10 14:38:41.364439

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of pairs of first and last names.
- The first names in the input data are varied and unique.
- The last names in the input data are also varied and unique.

Summary for Output Column Data:
- The output column data consists of the last name followed by the first initial, separated by a comma and a space.
- The output column data follows a consistent format of Last Name, First Initial.

Relationship between Input and Output:
- The output column data is derived from the input column data by rearranging the order of the names and including only the last name followed by the first initial.
- The output column data maintains the uniqueness of the last names from the input data.
- The output column data provides a concise and standardized representation of the input data, making it easier to identify individuals based on their last names., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(first_name, last_name):
    # Rearrange the names and format the output
    output = last_name + ', ' + first_name[0] + '.'
    return output

# Test cases
print(generated_function('Launa', 'Withers'))
print(generated_function('Lakenya', 'Edison'))
print(generated_function('Brendan', 'Hage'))
print(generated_function('Bradford', 'Lango'))
print(generated_function('Rudolf', 'Akiyama'))
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.

# End time: 2024-04-10 14:38:43.429835
# Elapsed time in seconds: 2.06534970000007