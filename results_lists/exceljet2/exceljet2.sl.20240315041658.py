def return_last_domain(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item.split('.')[-1])
    return output_list

input_list = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(return_last_domain(input_list))
