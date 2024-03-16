def extract_numbers(input_list):
    output = []
    for item in input_list:
        num = ''.join(filter(str.isdigit, item[0]))
        output.append(num)
    return output

input_data = [['80v', '3'], ['10hrs', '3'], ['7h', '2'], ['500m', '4']]
print(extract_numbers(input_data))
