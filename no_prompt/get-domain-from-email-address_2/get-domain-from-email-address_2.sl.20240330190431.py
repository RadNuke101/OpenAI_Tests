# Start time: 2024-03-30 19:15:24.564891

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_username(email: str) -> str:
    try:
        # Split the email address by '@' to separate the username and domain
        username, domain = email.split('@')
        
        # Split the username by '_' to extract the desired username part
        username_parts = username.split('_')
        
        # Check if the username has multiple parts
        if len(username_parts) > 1:
            return username_parts[0]
        else:
            return username
    except ValueError:
        print("Invalid email format. Please provide a valid email address.")
        return ""

# Test cases
print(extract_username('ann chang_maaker.com'))  # Output: ann
print(extract_username('bobby smith_bobt_sphynx.uk.co'))  # Output: bobt
print(extract_username('art lennox_art.lennox_svxn.com'))  # Output: art.lennox

# End time: 2024-03-30 19:15:26.846849
# Elapsed time in seconds: 2.281899599999633