def format_names(input_list):
    output = []
    for pair in input_list:
        output.append(pair[0] + ' ' + pair[1][0] + '.')
    return output
