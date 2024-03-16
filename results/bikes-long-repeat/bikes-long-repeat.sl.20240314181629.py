def get_text_before_last_3_numbers(input_list):
    output_list = []
    for item in input_list:
        text = item[0][:-3]
        output_list.append(text)
    return output_list
