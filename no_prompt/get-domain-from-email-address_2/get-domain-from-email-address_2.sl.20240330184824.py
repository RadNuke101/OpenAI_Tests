# Start time: 2024-03-30 18:59:37.571451

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'ann chang', 'achang_maaker.com'
# Output: 'achang'

# Input: 'bobby smith', 'bobt_sphynx.uk.co'
# Output: 'bobt'

# Input: 'art lennox', 'art.lennox_svxn.com'
# Output: 'art.lennox'

def extract_username(full_name, email):
    try:
        # Split full name into first name and last name
        first_name, last_name = full_name.split()
        
        # Extract username from email
        username = email.split('@')[0]
        
        # Check if username contains underscore
        if '_' in username:
            username = username.split('_')[0]
        
        return username
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(extract_username('ann chang', 'achang_maaker.com'))
print(extract_username('bobby smith', 'bobt_sphynx.uk.co'))
print(extract_username('art lennox', 'art.lennox_svxn.com'))

# End time: 2024-03-30 18:59:40.768242
# Elapsed time in seconds: 3.1967201700001624