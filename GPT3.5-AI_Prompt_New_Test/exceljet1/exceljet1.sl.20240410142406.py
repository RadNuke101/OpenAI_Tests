# Start time: 2024-04-10 14:34:35.823788

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (Full Names):
- The input column contains full names in the format of first name followed by last name, separated by a space.
- The names in the input column appear to be a combination of common first names and last names.

Summary for Input Column 2 (Email Domains):
- The input column contains email addresses with domains in the format of domain.com or domain.co.uk.
- The email domains in the input column seem to be a mix of common domain extensions like .com and .co.uk.

Summary for Output Column (Extracted Domain):
- The output column contains extracted domain names from the email addresses in the input column.
- The extracted domains in the output column appear to be the last part of the email addresses after the underscore symbol.

Relationship between Input and Output:
- The output column consists of the domain names extracted from the email addresses provided in the input column.
- The extraction process involves taking the text after the underscore symbol in the email address and considering it as the domain name.
- There is a clear relationship between the input email addresses and the output extracted domains, where the last part of the email address after the underscore is extracted as the domain name., and input as ['ann chang', 'achang_maaker.com'] output is maaker.com, input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(full_name, email_domain):
    # Split the full name into first name and last name
    first_name, last_name = full_name.split()
    
    # Extract the domain name from the email address
    extracted_domain = email_domain.split('_')[-1]
    
    return extracted_domain

# Test cases
print(generated_function('ann chang', 'achang_maaker.com'))  # Output: maaker.com
print(generated_function('bobby smith', 'bobt_sphynx.uk.co'))  # Output: sphynx.uk.co
print(generated_function('art lennox', 'art.lennox_svxn.com'))  # Output: svxn.com
print(generated_function('smith bagshaw', 'smith_bbbbb.com'))  # Output: bbbbb.com
print(generated_function("ann chang", "achang_maaker.com"))  ## Output: maaker.com
print(generated_function("bobby smith", "bobt_sphynx.uk.co"))  ## Output: sphynx.uk.co
print(generated_function("art lennox", "art.lennox_svxn.com"))  ## Output: svxn.com
print(generated_function("smith bagshaw", "smith_bbbbb.com"))  ## Output: bbbbb.com

# End time: 2024-04-10 14:34:38.347078
# Elapsed time in seconds: 2.523234398999989


# APPEND TEST SCRIPTS...
print(generated_function("ann chang", "achang_maaker.com"))  ## Output: maaker.com
print(generated_function("bobby smith", "bobt_sphynx.uk.co"))  ## Output: sphynx.uk.co
print(generated_function("art lennox", "art.lennox_svxn.com"))  ## Output: svxn.com
print(generated_function("smith bagshaw", "smith_bbbbb.com"))  ## Output: bbbbb.com


print(generated_function("art lennox", "art.lennox_abcd.gov.us"))  ### Output: abcd.gov.us
print(generated_function("ann chang", "achang_maaker.edu"))  ### Output: maaker.edu
print(generated_function("bobby smith", "bobt_sphynx.fr.co"))  ### Output: sphynx.fr.co
print(generated_function("smith bagshaw", "smith_banana.apple.com"))  ### Output: banana.apple.com

# TEST SCRIPTS APPENDED!

