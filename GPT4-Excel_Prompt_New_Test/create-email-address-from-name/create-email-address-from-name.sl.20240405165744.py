# Start time: 2024-04-05 17:09:43.774208

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end , and input as ['brown', 'traci'] output is tbrown_acme.com, input as ['thomas', 'linda'] output is lthomas_acme.com, input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_input, second_input):
    # Take the first letter of the second input
    first_letter_second_input = second_input[0]
    # Add it to the front of the first input
    modified_first_input = first_letter_second_input + first_input
    # Add "_acme.com" at the end
    result = modified_first_input + "_acme.com"
    return result

# Test cases
output1 = generated_function('brown', 'traci')
output2 = generated_function('thomas', 'linda')
output3 = generated_function('ward', 'jack')
print(generated_function("brown", "traci"))  ## Output: tbrown_acme.com
print(generated_function("thomas", "linda"))  ## Output: lthomas_acme.com
print(generated_function("ward", "jack"))  ## Output: jward_acme.com

# End time: 2024-04-05 17:09:49.117767
# Elapsed time in seconds: 5.3433767510005055


# APPEND TEST SCRIPTS...
print(generated_function("brown", "traci"))  ## Output: tbrown_acme.com
print(generated_function("thomas", "linda"))  ## Output: lthomas_acme.com
print(generated_function("ward", "jack"))  ## Output: jward_acme.com


print(generated_function("reynolds", "olivia"))  ### Output: oreynolds_acme.com
print(generated_function("anderson", "jackson"))  ### Output: janderson_acme.com

# TEST SCRIPTS APPENDED!

