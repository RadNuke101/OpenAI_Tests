def format_names(input_list):
    output = []
    for names in input_list:
        output.append(names[0] + ' ' + names[1][0] + '.')
    return output
