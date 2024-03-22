# Prompt: return everything after the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: maaker.com

def extract_domain(input_data):
    name, email = input_data.split()
    return email.split('_')[1]

# Test cases
print(extract_domain('ann chang achang_maaker.com'))  # Output: maaker.com
print(extract_domain('bobby smith bobt_sphynx.uk.co'))  # Output: sphynx.uk.co
print(extract_domain('art lennox art.lennox_svxn.com'))  # Output: svxn.com
print(extract_domain('smith bagshaw smith_bbbbb.com'))  # Output: bbbbb.com
