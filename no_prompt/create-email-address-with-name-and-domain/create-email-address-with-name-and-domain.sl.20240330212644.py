# Start time: 2024-03-30 21:27:55.525326

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def generate_username(first_name, last_name, domain):
    try:
        username = first_name[0] + last_name
        username = username.lower().replace(" ", "_") + "_" + domain
        return username
    except Exception as e:
        print("Error: Invalid input format")

# Test cases
# print(generate_username('ayako', 'ogawa', 'acme.com'))  # aogawa_acme.com
# print(generate_username('amy', 'johnson', 'google.com'))  # ajohnson_google.com
# print(generate_username('tom', 'chang', 'upenn.edu'))  # tchang_upenn.edu

# End time: 2024-03-30 21:27:58.708623
# Elapsed time in seconds: 3.1831898930013267