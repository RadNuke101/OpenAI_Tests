# Start time: 2024-03-30 18:26:36.978387

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'ann chang', 'achang_maaker.com'
# Output: 'achang'

def extract_username(name, email):
    try:
        # Split the email address at the underscore
        username = email.split('_')[0]
        return username
    except (AttributeError, IndexError):
        return "Invalid input"

# Test cases
print(extract_username('ann chang', 'achang_maaker.com'))  # Output: achang
print(extract_username('bobby smith', 'bobt_sphynx.uk.co'))  # Output: bobt
print(extract_username('art lennox', 'art.lennox_svxn.com'))  # Output: art.lennox

# End time: 2024-03-30 18:26:39.877098
# Elapsed time in seconds: 2.8986581640000395