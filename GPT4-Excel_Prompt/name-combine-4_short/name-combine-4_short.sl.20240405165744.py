# Start time: 2024-04-05 17:22:13.489719

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name):
    # Return the formatted string as per the instructions
    return f"{last_name}, {first_name[0]}."

# Test cases based on the provided examples
output1 = generated_function('Launa', 'Withers')
print(output1)  # Expected: Withers, L.

output2 = generated_function('Lakenya', 'Edison')
print(output2)  # Expected: Edison, L.

output3 = generated_function('Brendan', 'Hage')
print(output3)  # Expected: Hage, B.

output4 = generated_function('Bradford', 'Lango')
print(output4)  # Expected: Lango, B.

output5 = generated_function('Rudolf', 'Akiyama')
print(output5)  # Expected: Akiyama, R.
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.

# End time: 2024-04-05 17:22:18.189503
# Elapsed time in seconds: 4.6996509000000515