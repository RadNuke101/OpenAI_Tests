# Start time: 2024-03-30 23:05:40.094459

# Content: Given that given input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, given input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, given input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# input: ['ayako', 'ogawa', 'acme.com']
# output: aogawa_acme.com

# input: ['amy', 'johnson', 'google.com']
# output: ajohnson_google.com

# input: ['tom', 'chang', 'upenn.edu']
# output: tchang_upenn.edu

def generate_username_email(input_list):
    try:
        if len(input_list) != 3:
            raise ValueError("Input list must contain exactly 3 elements")
        
        first_name = input_list[0]
        last_name = input_list[1]
        domain = input_list[2]
        
        username = first_name[0] + last_name
        email = last_name + "_" + domain
        
        return username + "_" + email
    except (IndexError, ValueError) as e:
        return "Invalid input"

# Test the function with the provided test cases
print(generate_username_email(['ayako', 'ogawa', 'acme.com']))
print(generate_username_email(['amy', 'johnson', 'google.com']))
print(generate_username_email(['tom', 'chang', 'upenn.edu']))

# End time: 2024-03-30 23:05:44.855778
# Elapsed time in seconds: 4.7615463950023695