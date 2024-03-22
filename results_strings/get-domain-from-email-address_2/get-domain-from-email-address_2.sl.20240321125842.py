# Prompt: return everything before the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: achang

def extract_text(input_data):
    second_input = input_data.split()[1]
    output = second_input.split('_')[0]
    return output

# Test cases
print(extract_text('ann chang achang_maaker.com'))  # Output: achang
print(extract_text('bobby smith bobt_sphynx.uk.co'))  # Output: bobt
print(extract_text('art lennox art.lennox_svxn.com'))  # Output: art.lennox
achang
bobt
art.lennox
