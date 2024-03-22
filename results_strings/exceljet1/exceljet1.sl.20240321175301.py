# Prompt: return everything after the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: maaker.com

def extract_domain(input_data):
    parts = input_data.split('_')
    return parts[1]

# Test cases
print(extract_domain('ann chang_achang_maaker.com'))  # Output: maaker.com
print(extract_domain('bobby smith_bobt_sphynx.uk.co'))  # Output: sphynx.uk.co
print(extract_domain('art lennox_art.lennox_svxn.com'))  # Output: svxn.com
print(extract_domain('smith bagshaw_smith_bbbbb.com'))  # Output: bbbbb.com
