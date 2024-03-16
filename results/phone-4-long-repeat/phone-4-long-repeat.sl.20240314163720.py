def replace_dash_with_dot(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item.replace("-", "."))
    return output_list
