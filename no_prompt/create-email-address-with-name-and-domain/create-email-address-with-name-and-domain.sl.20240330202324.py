# Start time: 2024-03-30 20:24:51.409306

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
        first_name = input_list[0][0]
        last_name = input_list[1]
        domain = input_list[2]
        
        return first_name + last_name + '_' + domain
    except IndexError:
        print("Input list should contain at least 3 elements")
    except TypeError:
        print("Input should be a list")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# print(generate_username_email(['ayako', 'ogawa', 'acme.com']))
# print(generate_username_email(['amy', 'johnson', 'google.com']))
# print(generate_username_email(['tom', 'chang', 'upenn.edu']))

# End time: 2024-03-30 20:24:54.457877
# Elapsed time in seconds: 3.0484881710008267