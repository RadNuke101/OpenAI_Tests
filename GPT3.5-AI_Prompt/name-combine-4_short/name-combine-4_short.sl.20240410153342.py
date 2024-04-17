# Start time: 2024-04-10 15:47:50.947195

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of pairs of first and last names.
- The first names in the input data are varied and unique.
- The last names in the input data are also varied and unique.

Summary for Output Column Data:
- The output column data consists of last names followed by the first initial of the first name, separated by a comma and a space.
- The output format is consistent across all entries, with the last name appearing first followed by the first initial of the first name.

Relationship between Input and Output:
- The relationship between the input and output is that the last name from the input data is used as the first part of the output, followed by a comma and space, and then the first initial of the first name from the input data.
- The output column data is derived from the input column data by rearranging and formatting the names in a specific way.
- The output provides a concise and standardized representation of the input data, with the last name taking precedence in the output format., and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    # Combine last name, comma, space, and first initial of first name
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

# End time: 2024-04-10 15:47:52.495255
# Elapsed time in seconds: 1.5480254450003486