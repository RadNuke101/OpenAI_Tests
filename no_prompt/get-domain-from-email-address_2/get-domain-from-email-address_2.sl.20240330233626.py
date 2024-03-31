# Start time: 2024-03-30 23:47:36.077402

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'ann chang', 'achang_maaker.com'
# Output: achang

def extract_username(name, email):
    try:
        # Split the email address by underscore
        parts = email.split('_')
        
        # Extract the first part before underscore
        username = parts[0]
        
        return username
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
print(extract_username('ann chang', 'achang_maaker.com'))  # Output: achang
print(extract_username('bobby smith', 'bobt_sphynx.uk.co'))  # Output: bobt
print(extract_username('art lennox', 'art.lennox_svxn.com'))  # Output: art.lennox

# End time: 2024-03-30 23:47:40.126073
# Elapsed time in seconds: 4.048605676001898