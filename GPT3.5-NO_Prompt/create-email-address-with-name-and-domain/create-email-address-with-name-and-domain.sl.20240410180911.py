# Start time: 2024-04-10 18:10:14.370039

'''
Prompt:
Given that input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(first_name, last_name, domain):
    try:
        output = f"{first_name[0]}{last_name}_{domain}"
        return output
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('ayako', 'ogawa', 'acme.com'))
print(generated_function('amy', 'johnson', 'google.com'))
print(generated_function('tom', 'chang', 'upenn.edu'))
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-10 18:10:15.899055
# Elapsed time in seconds: 1.5289894769998682