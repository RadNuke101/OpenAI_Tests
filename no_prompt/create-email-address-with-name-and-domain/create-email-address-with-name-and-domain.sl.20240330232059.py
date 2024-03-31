# Start time: 2024-03-30 23:21:53.214364

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'ayako', 'ogawa', 'acme.com'
# Output: 'aogawa_acme.com'

def combine_names(email):
    try:
        first_name, last_name, domain = email.split(',')
        return first_name[0] + last_name + '_' + domain
    except Exception as e:
        print("Error: Invalid input format")

# Test cases
print(combine_names('ayako,ogawa,acme.com'))  # aogawa_acme.com
print(combine_names('amy,johnson,google.com'))  # ajohnson_google.com
print(combine_names('tom,chang,upenn.edu'))  # tchang_upenn.edu

# End time: 2024-03-30 23:21:55.279482
# Elapsed time in seconds: 2.065064156999142