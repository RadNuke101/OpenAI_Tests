def get_last_domain_extension(input_list):
    output_list = []
    for item in input_list:
        last_dot_index = item[0].rfind('.')
        output_list.append(item[0][last_dot_index+1:])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(get_last_domain_extension(input_list))
