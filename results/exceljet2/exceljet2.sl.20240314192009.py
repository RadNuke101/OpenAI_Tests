def return_last_extension(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('.')[-1])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(return_last_extension(input_list))
