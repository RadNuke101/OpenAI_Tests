# Start time: 2024-03-30 19:20:11.855350

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# Input: ['ayako', 'ogawa', 'acme.com']
# Output: aogawa_acme.com

# Input: ['amy', 'johnson', 'google.com']
# Output: ajohnson_google.com

# Input: ['tom', 'chang', 'upenn.edu']
# Output: tchang_upenn.edu

def combine_names(input_list):
    try:
        first_name = input_list[0][0]
        last_name = input_list[1]
        domain = input_list[2]
        return first_name + last_name + '_' + domain
    except (IndexError, TypeError):
        return "Invalid input format"

# Test Cases
print(combine_names(['ayako', 'ogawa', 'acme.com']))
print(combine_names(['amy', 'johnson', 'google.com']))
print(combine_names(['tom', 'chang', 'upenn.edu']))

# End time: 2024-03-30 19:20:17.823094
# Elapsed time in seconds: 5.967566098000134