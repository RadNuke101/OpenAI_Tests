# Start time: 2024-04-10 17:40:56.389832

'''
Prompt:
Given that input as ['ann chang', 'achang_maaker.com'] output is maaker.com, input as ['bobby smith', 'bobt_sphynx.uk.co'] output is sphynx.uk.co, input as ['art lennox', 'art.lennox_svxn.com'] output is svxn.com, input as ['smith bagshaw', 'smith_bbbbb.com'] output is bbbbb.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name, email):
    try:
        last_name = name.split()[1]
        domain = email.split('@')[1]
        output = domain.split('.')[-1]
        return output
    except IndexError:
        return "Invalid input"

# Test cases
print(generated_function('ann chang', 'achang_maaker.com'))
print(generated_function('bobby smith', 'bobt_sphynx.uk.co'))
print(generated_function('art lennox', 'art.lennox_svxn.com'))
print(generated_function('smith bagshaw', 'smith_bbbbb.com'))
print(generated_function("ann chang", "achang_maaker.com"))  ## Output: maaker.com
print(generated_function("bobby smith", "bobt_sphynx.uk.co"))  ## Output: sphynx.uk.co
print(generated_function("art lennox", "art.lennox_svxn.com"))  ## Output: svxn.com
print(generated_function("smith bagshaw", "smith_bbbbb.com"))  ## Output: bbbbb.com

# End time: 2024-04-10 17:40:58.269311
# Elapsed time in seconds: 1.8794556929999544


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

