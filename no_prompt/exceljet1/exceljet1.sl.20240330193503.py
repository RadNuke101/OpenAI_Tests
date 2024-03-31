# Start time: 2024-03-30 19:42:58.687913

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is maaker.com, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, given input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, given input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain_name(name, email):
    try:
        # Split the email address by underscore and take the last part
        domain = email.split('_')[-1]
        return domain
    except:
        return "Invalid input"

# Test cases
print(extract_domain_name('ann chang', 'achang_maaker.com'))  # Output should be maaker.com
print(extract_domain_name('bobby smith', 'bobt_sphynx.uk.co'))  # Output should be sphynx.uk.co
print(extract_domain_name('art lennox', 'art.lennox_svxn.com'))  # Output should be svxn.com
print(extract_domain_name('smith bagshaw', 'smith_bbbbb.com'))  # Output should be bbbbb.com

# End time: 2024-03-30 19:43:03.292531
# Elapsed time in seconds: 4.604566105999766