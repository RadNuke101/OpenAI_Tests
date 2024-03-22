def get_domain_after_underscore(input_list):
    output = []
    for item in input_list:
        domain = item[1].split('_')[1]
        output.append(domain)
    return output

input_list = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com'], ['smith bagshaw', 'smith_bbbbb.com']]
print(get_domain_after_underscore(input_list))
