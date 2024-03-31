# Start time: 2024-03-30 18:16:52.372852

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# input: 'ayako', 'ogawa', 'acme.com' => output: 'aogawa_acme.com'
# input: 'amy', 'johnson', 'google.com' => output: 'ajohnson_google.com'
# input: 'tom', 'chang', 'upenn.edu' => output: 'tchang_upenn.edu'

def combine_names(first_name, last_name, domain):
    try:
        # Concatenate the first letter of the first name with the last name and add an underscore
        result = first_name[0] + last_name + '_' + domain
        return result
    except Exception as e:
        print("Error:", e)

# Test Cases
print(combine_names('ayako', 'ogawa', 'acme.com'))
print(combine_names('amy', 'johnson', 'google.com'))
print(combine_names('tom', 'chang', 'upenn.edu'))

# End time: 2024-03-30 18:16:54.852565
# Elapsed time in seconds: 2.479655987000001