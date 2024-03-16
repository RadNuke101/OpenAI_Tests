def format_names(input_list):
    output = []
    for names in input_list:
        output.append(names[1] + ', ' + names[0][0] + '.')
    return output
