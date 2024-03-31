# Start time: 2024-03-30 19:26:38.632117

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is maaker.com, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, given input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, given input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain(input_str):
    try:
        name, domain = input_str.split(' ')
        return domain.split('.')[-1]
    except (ValueError, IndexError):
        return "Invalid input format"

# Test cases
# print(extract_domain('ann chang achang_maaker.com'))  # Output: maaker.com
# print(extract_domain('bobby smith bobt_sphynx.uk.co'))  # Output: sphynx.uk.co
# print(extract_domain('art lennox art.lennox_svxn.com'))  # Output: svxn.com
# print(extract_domain('smith bagshaw smith_bbbbb.com'))  # Output: bbbbb.com

# End time: 2024-03-30 19:26:41.177579
# Elapsed time in seconds: 2.545382810999854