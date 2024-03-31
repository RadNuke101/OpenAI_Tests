# Start time: 2024-03-30 19:30:04.685456

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_username(name_email):
    try:
        name, email = name_email.split()
        username = email.split('@')[0]
        if '_' in username:
            username = username.split('_')[0]
        return username
    except (ValueError, IndexError):
        return "Invalid input format"

# Test cases
print(extract_username('ann chang achang_maaker.com'))  # Output: achang
print(extract_username('bobby smith bobt_sphynx.uk.co'))  # Output: bobt
print(extract_username('art lennox art.lennox_svxn.com'))  # Output: art.lennox

# End time: 2024-03-30 19:30:07.393366
# Elapsed time in seconds: 2.707834647999789