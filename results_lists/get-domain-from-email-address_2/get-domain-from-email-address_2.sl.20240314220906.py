def extract_username(data):
    return [info[1].split('_')[0] for info in data]

input_data = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
output = extract_username(input_data)
print(output)
