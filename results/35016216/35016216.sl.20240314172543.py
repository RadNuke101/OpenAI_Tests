def process_input(input_list):
    output_list = []
    for item in input_list:
        if 'C0' in item[0]:
            output_list.extend(item)
    return output_list
