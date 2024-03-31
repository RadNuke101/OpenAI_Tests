# Start time: 2024-03-30 20:40:16.373661

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# Input: 'ayako', 'ogawa', 'acme.com'
# Output: aogawa_acme.com

# Input: 'amy', 'johnson', 'google.com'
# Output: ajohnson_google.com

# Input: 'tom', 'chang', 'upenn.edu'
# Output: tchang_upenn.edu

def generate_username(email, last_name):
    try:
        first_initial = email[0]
        last_name = last_name.replace(' ', '')
        domain = email.split('@')[1]
        return first_initial + last_name + '_' + domain
    except Exception as e:
        print("Error:", e)

# Test cases
print(generate_username('ayako', 'ogawa'))
print(generate_username('amy', 'johnson'))
print(generate_username('tom', 'chang'))

# End time: 2024-03-30 20:40:21.818403
# Elapsed time in seconds: 5.444602401999873