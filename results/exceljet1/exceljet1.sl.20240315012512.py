def get_domain(input_list):
    return [item[1].split('_')[1] for item in input_list]

input_list = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com'], ['smith bagshaw', 'smith_bbbbb.com']]
print(get_domain(input_list))
