def return_expression_or_second(input_list):
    output_list = []
    for pair in input_list:
        if 'C0' in pair[0]:
            output_list.extend(pair)
    return output_list
