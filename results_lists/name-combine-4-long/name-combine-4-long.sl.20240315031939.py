def format_names(input_list):
    output_list = []
    for name in input_list:
        output_list.append(name[1] + ', ' + name[0][0] + '.')
    return output_list
