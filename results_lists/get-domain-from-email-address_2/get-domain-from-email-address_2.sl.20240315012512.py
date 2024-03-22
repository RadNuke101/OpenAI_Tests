def get_prefixes(data):
    prefixes = []
    for item in data:
        name = item[1].split('_')[0]
        prefixes.append(name)
    return prefixes

input_data = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
output = get_prefixes(input_data)
print(output)
