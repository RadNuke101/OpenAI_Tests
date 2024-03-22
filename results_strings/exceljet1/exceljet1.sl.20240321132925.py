# Prompt: return everything after the "_" in the second input
# Input: ['ann chang', 'achang_maaker.com']
# Output: maaker.com

def get_second_input_suffix(input_list):
    second_input = input_list[1]
    suffix = second_input.split('_')[1]
    return suffix

# Test cases
print(get_second_input_suffix(['ann chang', 'achang_maaker.com']))  # Output: maaker.com
print(get_second_input_suffix(['bobby smith', 'bobt_sphynx.uk.co']))  # Output: sphynx.uk.co
print(get_second_input_suffix(['art lennox', 'art.lennox_svxn.com']))  # Output: svxn.com
print(get_second_input_suffix(['smith bagshaw', 'smith_bbbbb.com']))  # Output: bbbbb.com
