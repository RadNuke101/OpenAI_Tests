def get_last_domain(input_list):
    output_list = []
    for item in input_list:
        domain = item[0].split('.')[-1]
        output_list.append(domain)
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(get_last_domain(input_list))
