def extract_numbers(input_list):
    output = []
    for item in input_list:
        number = ''.join(filter(str.isdigit, item[0]))
        output.append(number)
    return output

input_list = [['80v', '3'], ['10hrs', '3'], ['7h', '2'], ['500m', '4']]
print(extract_numbers(input_list))  # Output: ['80', '10', '7', '500']
