def extract_username(data):
    return [item[1].split('_')[0] if '_' in item[1] else item[1] for item in data]

input_data = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
output = extract_username(input_data)
print(output)
