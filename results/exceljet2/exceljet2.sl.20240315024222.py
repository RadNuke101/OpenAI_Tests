def get_last_domain_parts(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            parts = item.split('.')
            output_list.append(parts[-1])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
output = get_last_domain_parts(input_list)
print(output)
