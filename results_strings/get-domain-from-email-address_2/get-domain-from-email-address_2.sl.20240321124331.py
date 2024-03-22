# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def get_prefix(input_str):
    inputs = input_str.split(',')
    name = inputs[0]
    email = inputs[1]
    
    prefix = email.split('_')[0]
    
    return prefix

# Test cases
print(get_prefix('ann chang,achang_maaker.com'))  # Output: achang
print(get_prefix('bobby smith,bobt_sphynx.uk.co'))  # Output: bobt
print(get_prefix('art lennox,art.lennox_svxn.com'))  # Output: art.lennox
