def format_phone_numbers(input_list):
    output_list = []
    for item in input_list:
        phone_number = item[0]
        first_three_nums = phone_number.split('-')[0][:3]
        formatted_number = phone_number.replace('-', ' ', 1).replace(first_three_nums, f'({first_three_nums})', 1)
        output_list.append(formatted_number)
    return output_list
