def return_expression_or_second(input_list):
    output = []
    for pair in input_list:
        if 'C0' in pair[0]:
            output.extend(pair)
    return output
