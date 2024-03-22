# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def get_prefix(input_str):
    parts = input_str.split('_')
    return parts[0]

# Test cases
print(get_prefix('ann chang_aaker.com'))  # Output: aaker
print(get_prefix('bobby smith_bobt_sphynx.uk.co'))  # Output: bobt
print(get_prefix('art lennox_art.lennox_svxn.com'))  # Output: art.lennox
