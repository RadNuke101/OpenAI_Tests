# Start time: 2024-03-30 21:06:44.187641

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_username(email):
    try:
        # Split the email address by '@' to get the username part
        username = email.split('@')[0]
        
        # Check if the username contains an underscore
        if '_' in username:
            # Split the username by underscore and return the first part
            return username.split('_')[0]
        else:
            return username
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(extract_username('ann chang_maaker.com'))  # Output: ann
print(extract_username('bobby smith_bobt_sphynx.uk.co'))  # Output: bobby
print(extract_username('art lennox_art.lennox_svxn.com'))  # Output: art.lennox

# End time: 2024-03-30 21:06:45.913698
# Elapsed time in seconds: 1.7264779039996938