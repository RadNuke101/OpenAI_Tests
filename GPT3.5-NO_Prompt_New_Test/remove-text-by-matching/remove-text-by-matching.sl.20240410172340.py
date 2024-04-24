# Start time: 2024-04-10 17:26:29.310432

'''
Prompt:
Given that input as ['801-345-1987'] output is 8013451987, input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(phone_number):
    try:
        # Remove any hyphens from the input phone number
        phone_number = phone_number.replace('-', '')
        
        # Convert the cleaned phone number to an integer and return it
        return int(phone_number)
    
    except ValueError:
        print("Invalid input. Please provide a valid phone number.")
        return None

# Test cases
generated_function('801-345-1987')
generated_function('612-554-2000')
print(generated_function("801-345-1987"))  ## Output: 8013451987
print(generated_function("612-554-2000"))  ## Output: 6125542000

# End time: 2024-04-10 17:26:30.867482
# Elapsed time in seconds: 1.557014258999999


# APPEND TEST SCRIPTS...
print(generated_function("801-345-1987"))  ## Output: 8013451987
print(generated_function("612-554-2000"))  ## Output: 6125542000


print(generated_function("345-801-1987"))  ### Output: 3458011987
print(generated_function("554-612-2000"))  ### Output: 5546122000

# TEST SCRIPTS APPENDED!

