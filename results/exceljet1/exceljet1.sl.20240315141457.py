def get_domain(input_lst):
    return [item[1].split('_')[1] for item in input_lst]

input_lst = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com'], ['smith bagshaw', 'smith_bbbbb.com']]
output = get_domain(input_lst)
print(output)
