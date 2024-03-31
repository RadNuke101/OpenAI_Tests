# Start time: 2024-03-30 23:00:01.038340

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is achang, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is bobt, given input as ['art lennox', 'art.lennox_svxn.com'] output is art.lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_username(input_str):
    try:
        # Split the input string into name and email parts
        name, email = input_str.split(' ')
        
        # Extract the username from the email
        username = email.split('@')[0]
        
        # Check if the username contains an underscore
        if '_' in username:
            # Split the username at the underscore and take the first part
            username = username.split('_')[0]
        
        return username
    except Exception as e:
        return "Invalid input"

# Test cases
print(extract_username('ann chang achang_maaker.com'))  # Output should be achang
print(extract_username('bobby smith bobt_sphynx.uk.co'))  # Output should be bobt
print(extract_username('art lennox art.lennox_svxn.com'))  # Output should be art.lennox

# End time: 2024-03-30 23:00:06.178642
# Elapsed time in seconds: 5.1401845939999475