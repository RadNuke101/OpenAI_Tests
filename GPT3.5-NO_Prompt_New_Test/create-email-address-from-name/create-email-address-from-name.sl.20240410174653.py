# Start time: 2024-04-10 17:50:07.237654

'''
Prompt:
Given that input as ['brown', 'traci'] output is tbrown_acme.com, input as ['thomas', 'linda'] output is lthomas_acme.com, input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        first_name = input_list[0].strip()
        last_name = input_list[1].strip()
        return last_name[0] + first_name + '_acme.com'
    except (IndexError, AttributeError):
        return "Invalid input format. Please provide two names separated by a comma."

# Test cases
print(generated_function('brown, traci'))
print(generated_function('thomas, linda'))
print(generated_function('ward, jack'))
print(generated_function("brown", "traci"))  ## Output: tbrown_acme.com
print(generated_function("thomas", "linda"))  ## Output: lthomas_acme.com
print(generated_function("ward", "jack"))  ## Output: jward_acme.com

# End time: 2024-04-10 17:50:09.074262
# Elapsed time in seconds: 1.836561015999905


# APPEND TEST SCRIPTS...
print(generated_function("brown", "traci"))  ## Output: tbrown_acme.com
print(generated_function("thomas", "linda"))  ## Output: lthomas_acme.com
print(generated_function("ward", "jack"))  ## Output: jward_acme.com


print(generated_function("reynolds", "olivia"))  ### Output: oreynolds_acme.com
print(generated_function("anderson", "jackson"))  ### Output: janderson_acme.com

# TEST SCRIPTS APPENDED!

