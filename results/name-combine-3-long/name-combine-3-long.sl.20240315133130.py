def format_names(input_list):
    output_list = []
    for name in input_list:
        formatted_name = name[0][0] + '. ' + name[1]
        output_list.append(formatted_name)
    return output_list
