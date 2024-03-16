def format_names(input_list):
    output_list = []
    for pair in input_list:
        output_list.append(pair[0] + ' ' + pair[1][0] + '.')
    return output_list
