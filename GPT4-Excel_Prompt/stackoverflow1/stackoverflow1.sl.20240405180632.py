# Start time: 2024-04-05 18:12:16.626265

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Find the index of " Inc" in the input string
    index = input_string.find(" Inc")
    # If " Inc" is found, return the substring up to that point
    if index != -1:
        return input_string[:index]
    # If " Inc" is not found, return the original string
    return input_string

# Test cases
print(generated_function('Trucking Inc.'))  # Expected output: Trucking
print(generated_function('New Truck Inc'))  # Expected output: New Truck
print(generated_function('ABV Trucking Inc, LLC'))  # Expected output: ABV Trucking
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-05 18:12:21.106856
# Elapsed time in seconds: 4.480457458999808