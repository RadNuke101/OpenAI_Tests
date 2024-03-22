# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_string(input_str):
    inputs = input_str.split(', ')
    name = inputs[0]
    email = inputs[1]
    
    return email.split('_')[0]

# Test cases
print(extract_string('ann chang, achang_maaker.com'))  # Output: achang
print(extract_string('bobby smith, bobt_sphynx.uk.co'))  # Output: bobt
print(extract_string('art lennox, art.lennox_svxn.com'))  # Output: art.lennox
