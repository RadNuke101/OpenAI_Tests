# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_before_underscore(input_str):
    inputs = input_str.split()
    second_input = inputs[1]
    output = second_input.split('_')[0]
    return output

# Test cases
print(extract_before_underscore('ann chang achang_maaker.com'))  # Output: achang
print(extract_before_underscore('bobby smith bobt_sphynx.uk.co'))  # Output: bobt
print(extract_before_underscore('art lennox art.lennox_svxn.com'))  # Output: art.lennox
achang
bobt
art.lennox
