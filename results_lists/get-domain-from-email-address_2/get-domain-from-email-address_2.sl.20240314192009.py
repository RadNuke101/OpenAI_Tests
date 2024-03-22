def extract_username(data):
    result = []
    for item in data:
        username = item[1].split('_')[0]
        result.append(username)
    return result

input_data = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
output = extract_username(input_data)
print(output)
