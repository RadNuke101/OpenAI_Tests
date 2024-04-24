# Start time: 2024-04-05 15:52:32.590465

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # Find the index of " Inc" in the company name
    index = company_name.find(" Inc")
    # If " Inc" is found, return the substring before it; otherwise, return the original company name
    if index != -1:
        return company_name[:index]
    else:
        return company_name

# Test cases
result1 = generated_function('Trucking Inc.')
result2 = generated_function('New Truck Inc')
result3 = generated_function('ABV Trucking Inc, LLC')

# The outputs of these test cases can be checked against the expected results
# but are not included in the code as per the instructions.
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-05 15:52:38.039610
# Elapsed time in seconds: 5.447124067000004


# APPEND TEST SCRIPTS...
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking


print(generated_function("New House Inc"))  ### Output: New House
print(generated_function("Brand New House Inc"))  ### Output: Brand New House
print(generated_function("Housing Inc."))  ### Output: Housing
print(generated_function("ABV Housing Inc, LLC"))  ### Output: ABV Housing

# TEST SCRIPTS APPENDED!

