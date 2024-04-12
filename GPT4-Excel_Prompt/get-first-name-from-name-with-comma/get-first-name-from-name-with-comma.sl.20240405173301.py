# Start time: 2024-04-05 17:35:59.798890

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string, option):
    # Split the input string by the comma
    parts = input_string.split(',')
    # Check the option and return the appropriate part of the string
    if option == '1':
        return parts[1]  # Return everything after the comma
    elif option == '2':
        return parts[0]  # Return everything before the comma
    else:
        return "Invalid option"  # Handle unexpected option values

# Test cases
print(generated_function('Chang,Amy', '1'))  # Expected output: Amy
print(generated_function('Chang,Amy', '2'))  # Expected output: Chang
print(generated_function('smith,bobby', '2'))  # Expected output: smith
print(generated_function('smith,bobby', '1'))  # Expected output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-05 17:36:06.097288
# Elapsed time in seconds: 6.298223309000605