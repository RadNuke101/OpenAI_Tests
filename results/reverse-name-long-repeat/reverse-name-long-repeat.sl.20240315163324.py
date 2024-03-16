def rearrange_names(input_list):
    output_list = []
    for names in input_list:
        output_list.append(names[1] + ' ' + names[0])
    return output_list
