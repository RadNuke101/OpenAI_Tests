def extract_prefix(input_list):
    output = []
    for item in input_list:
        output.append(item[1].split('_')[0])
    return output

input_list = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
print(extract_prefix(input_list))
