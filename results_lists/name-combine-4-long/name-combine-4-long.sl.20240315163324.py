def format_names(input_list):
    output_list = []
    for name in input_list:
        formatted_name = name[1] + ', ' + name[0][0] + '.'
        output_list.append(formatted_name)
    return output_list
