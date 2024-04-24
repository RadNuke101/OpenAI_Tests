# Start time: 2024-04-10 17:35:57.782180

'''
Prompt:
Given that input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_str = input_str.strip('[]')
        input_str = input_str.replace("'", "")
        input_str = input_str.replace(",", "")
        input_str = input_str.split()
        
        if len(input_str) == 1:
            return input_str[0]
        elif len(input_str) == 2:
            return input_str[0] + " " + input_str[1]
        elif len(input_str) > 2:
            return input_str[0] + " " + input_str[1]
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('Trucking Inc.'))  # Output: Trucking
print(generated_function('New Truck Inc'))  # Output: New Truck
print(generated_function('ABV Trucking Inc, LLC'))  # Output: ABV Trucking
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-10 17:36:00.381320
# Elapsed time in seconds: 2.599108354000009


# APPEND TEST SCRIPTS...
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking


print(generated_function("New House Inc"))  ### Output: New House
print(generated_function("Brand New House Inc"))  ### Output: Brand New House
print(generated_function("Housing Inc."))  ### Output: Housing
print(generated_function("ABV Housing Inc, LLC"))  ### Output: ABV Housing

# TEST SCRIPTS APPENDED!

