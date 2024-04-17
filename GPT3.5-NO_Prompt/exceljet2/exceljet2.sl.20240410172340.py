# Start time: 2024-04-10 17:29:40.225464

'''
Prompt:
Given that input as ['www.domain.com'] output is com, input as ['mail.net'] output is net, input as ['www.amaon.co.uk'] output is uk, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        domain = input_str.split('.')[-1]
        return domain
    except (AttributeError, IndexError):
        return "Invalid input"

# Test cases
print(generated_function('www.domain.com'))
print(generated_function('mail.net'))
print(generated_function('www.amaon.co.uk'))
print(generated_function("www.domain.com"))  ## Output: com
print(generated_function("mail.net"))  ## Output: net
print(generated_function("www.amaon.co.uk"))  ## Output: uk

# End time: 2024-04-10 17:29:41.544231
# Elapsed time in seconds: 1.3187394849999805