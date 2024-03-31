# Start time: 2024-03-30 21:43:42.103410

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# Input: 'ayako', 'ogawa', 'acme.com'
# Output: aogawa_acme.com

# Input: 'amy', 'johnson', 'google.com'
# Output: ajohnson_google.com

# Input: 'tom', 'chang', 'upenn.edu'
# Output: tchang_upenn.edu

def combine_names(first_name, last_name, domain):
    try:
        # Concatenate the first letter of the first name with the last name and add underscore
        result = first_name[0] + last_name + '_' + domain
        return result
    except Exception as e:
        print("Error:", e)

# Test cases
print(combine_names('ayako', 'ogawa', 'acme.com'))
print(combine_names('amy', 'johnson', 'google.com'))
print(combine_names('tom', 'chang', 'upenn.edu'))

# End time: 2024-03-30 21:43:46.734667
# Elapsed time in seconds: 4.631128201001047