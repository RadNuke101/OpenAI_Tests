# Start time: 2024-04-10 17:38:42.571382

'''
Prompt:
Given that input as ['801-345-1987'] output is 8013451987, input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(phone_number):
    try:
        # Remove any hyphens from the input phone number
        phone_number = phone_number.replace('-', '')
        
        # Convert the phone number to an integer and return
        return int(phone_number)
    
    except ValueError:
        print("Invalid input. Please provide a valid phone number.")
        return None

# Test cases
generated_function('801-345-1987')
generated_function('612-554-2000')
print(generated_function("801-345-1987"))  ## Output: 8013451987
print(generated_function("612-554-2000"))  ## Output: 6125542000

# End time: 2024-04-10 17:38:44.181625
# Elapsed time in seconds: 1.610221939999974