def get_last_domain_parts(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('.')[-1])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(get_last_domain_parts(input_list))
