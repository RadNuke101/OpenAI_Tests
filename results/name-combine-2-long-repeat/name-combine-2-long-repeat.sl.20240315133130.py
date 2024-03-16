def format_names(input_list):
    output = []
    for names in input_list:
        formatted_name = names[0] + ' ' + names[1][0] + '.'
        output.append(formatted_name)
    return output
