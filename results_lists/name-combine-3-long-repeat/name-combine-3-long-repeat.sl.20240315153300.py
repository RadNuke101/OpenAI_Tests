def first_letter_period_second_input(input_list):
    result = []
    for pair in input_list:
        result.append(pair[0][0] + '. ' + pair[1])
    return result
