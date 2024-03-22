def get_last_domain_parts(input_list):
    output_list = []
    for item in input_list:
        domain = item[0]
        last_dot_index = domain.rfind('.')
        if last_dot_index != -1:
            output_list.append(domain[last_dot_index + 1:])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(get_last_domain_parts(input_list))
