# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_string(input):
    parts = input.split('_')
    return parts[0]

# Test cases
print(extract_string('ann chang_a.chang@gmail.com'))  # Output: a.chang
print(extract_string('bobby smith_bobt_sphynx.uk.co'))  # Output: bobt
print(extract_string('art lennox_art.lennox_svxn.com'))  # Output: art.lennox
