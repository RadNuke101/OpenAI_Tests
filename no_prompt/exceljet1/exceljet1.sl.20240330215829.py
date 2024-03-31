# Start time: 2024-03-30 22:06:20.620212

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is maaker.com, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, given input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, given input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain(input_str):
    try:
        name, email = input_str.split(',')
        domain = email.split('@')[1]
        result = domain.split('.')[-1]
        return result
    except (ValueError, IndexError):
        return "Invalid input format"

# Test cases
# print(extract_domain('ann chang, achang_maaker.com'))  # maaker.com
# print(extract_domain('bobby smith, bobt_sphynx.uk.co'))  # sphynx.uk.co
# print(extract_domain('art lennox, art.lennox_svxn.com'))  # svxn.com
# print(extract_domain('smith bagshaw, smith_bbbbb.com'))  # bbbbb.com

# End time: 2024-03-30 22:06:23.946800
# Elapsed time in seconds: 3.326487113999974