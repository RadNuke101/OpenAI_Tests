def format_input(input_list):
    output_list = []
    for pair in input_list:
        if 'USA' not in pair[1]:
            output_list.append(pair[0] + ', ' + pair[1] + ', USA')
        else:
            output_list.append(pair[0] + ', ' + pair[1])
    return output_list
