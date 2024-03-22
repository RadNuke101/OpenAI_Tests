def extract_username(input_list):
    output_list = []
    for item in input_list:
        username = item[1].split('_')[0]
        output_list.append(username)
    return output_list

input_list = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com']]
print(extract_username(input_list))
