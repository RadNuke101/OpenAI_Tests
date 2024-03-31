# Start time: 2024-03-30 20:35:27.982625

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'ann chang', 'achang_maaker.com'
# Output: 'achang'

# Input: 'bobby smith', 'bobt_sphynx.uk.co'
# Output: 'bobt'

# Input: 'art lennox', 'art.lennox_svxn.com'
# Output: 'art.lennox'

def extract_username(name, email):
    try:
        # Split the email address by underscore and dot
        parts = email.split('_')
        parts = parts[0].split('.')
        
        # Check if the first part of the email is a substring of the name
        if parts[0] in name:
            return parts[0]
        else:
            return name.replace(' ', '.')
    except Exception as e:
        print("Error:", e)

# Test cases
print(extract_username('ann chang', 'achang_maaker.com'))
print(extract_username('bobby smith', 'bobt_sphynx.uk.co'))
print(extract_username('art lennox', 'art.lennox_svxn.com'))

# End time: 2024-03-30 20:35:31.550326
# Elapsed time in seconds: 3.5680102859996623