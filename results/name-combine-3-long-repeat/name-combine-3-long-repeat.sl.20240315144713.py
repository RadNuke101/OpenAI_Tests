def first_letter_period_second_input(input_list):
    output = []
    for pair in input_list:
        output.append(pair[0][0] + '. ' + pair[1])
    return output
