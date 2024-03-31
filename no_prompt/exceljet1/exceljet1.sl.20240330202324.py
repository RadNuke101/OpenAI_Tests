# Start time: 2024-03-30 20:31:56.404663

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is maaker.com, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, given input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, given input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'ann chang', 'achang_maaker.com'
# Output: maaker.com

# Input: 'bobby smith', 'bobt_sphynx.uk.co'
# Output: sphynx.uk.co

# Input: 'art lennox', 'art.lennox_svxn.com'
# Output: svxn.com

# Input: 'smith bagshaw', 'smith_bbbbb.com'
# Output: bbbbb.com

def extract_domain_name(full_name, email):
    try:
        # Split the email address by underscore
        parts = email.split('_')
        
        # Get the last part after splitting by underscore
        domain = parts[-1]
        
        return domain
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function with the provided test cases
print(extract_domain_name('ann chang', 'achang_maaker.com'))
print(extract_domain_name('bobby smith', 'bobt_sphynx.uk.co'))
print(extract_domain_name('art lennox', 'art.lennox_svxn.com'))
print(extract_domain_name('smith bagshaw', 'smith_bbbbb.com'))

# End time: 2024-03-30 20:31:58.852369
# Elapsed time in seconds: 2.44764491099977