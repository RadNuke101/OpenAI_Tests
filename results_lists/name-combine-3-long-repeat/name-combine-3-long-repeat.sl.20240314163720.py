def first_letter_period_second_input(input_list):
    output_list = []
    for pair in input_list:
        output_list.append(pair[0][0] + '. ' + pair[1])
    return output_list
