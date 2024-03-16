def get_last_domain_parts(input_list):
    output = []
    for item in input_list:
        domain = item[0]
        parts = domain.split('.')
        output.append(parts[-1])
    return output

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(get_last_domain_parts(input_list))
