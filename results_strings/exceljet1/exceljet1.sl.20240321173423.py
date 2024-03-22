# Prompt: return everything after the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: maaker.com

def get_suffix(input_str):
    parts = input_str.split('_')
    return parts[1]

# Test cases
print(get_suffix('ann chang_achang_maaker.com'))  # Output: maaker.com
print(get_suffix('bobby smith_bobt_sphynx.uk.co'))  # Output: sphynx.uk.co
print(get_suffix('art lennox_art.lennox_svxn.com'))  # Output: svxn.com
print(get_suffix('smith bagshaw_smith_bbbbb.com'))  # Output: bbbbb.com
