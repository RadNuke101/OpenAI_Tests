def format_phone_numbers(input_list):
    output_list = []
    for item in input_list:
        phone_number = item[0]
        formatted_number = '(' + phone_number[:3] + ') ' + phone_number[4:]
        output_list.append(formatted_number)
    return output_list
