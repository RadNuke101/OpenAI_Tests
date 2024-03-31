# Start time: 2024-03-30 20:15:23.742833

# Content: Given that given input as ['ann chang', 'achang_maaker.com'] output is maaker.com, given input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, given input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, given input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'ann chang', 'achang_maaker.com' => output: 'maaker.com'
# input: 'bobby smith', 'bobt_sphynx.uk.co' => output: 'sphynx.uk.co'
# input: 'art lennox', 'art.lennox_svxn.com' => output: 'svxn.com'
# input: 'smith bagshaw', 'smith_bbbbb.com' => output: 'bbbbb.com'

def extract_domain_name(full_name, email):
    try:
        # Split the email address by underscore
        parts = email.split('_')
        
        # Get the last part after splitting by underscore
        domain = parts[-1]
        
        return domain
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(extract_domain_name('ann chang', 'achang_maaker.com'))  # maaker.com
print(extract_domain_name('bobby smith', 'bobt_sphynx.uk.co'))  # sphynx.uk.co
print(extract_domain_name('art lennox', 'art.lennox_svxn.com'))  # svxn.com
print(extract_domain_name('smith bagshaw', 'smith_bbbbb.com'))  # bbbbb.com

# End time: 2024-03-30 20:15:25.800554
# Elapsed time in seconds: 2.0577002150002954