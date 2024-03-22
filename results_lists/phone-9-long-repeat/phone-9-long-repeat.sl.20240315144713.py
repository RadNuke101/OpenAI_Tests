def format_phone_numbers(input_list):
    output_list = []
    for sublist in input_list:
        phone_number = sublist[0]
        formatted_number = phone_number.replace("+", "").replace("-", ".").replace(" ", ".")
        output_list.append(formatted_number)
    return output_list
