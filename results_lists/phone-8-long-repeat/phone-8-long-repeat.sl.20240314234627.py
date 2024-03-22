def return_last_three_numbers(input_list):
    output = []
    for item in input_list:
        output.append(item[0][-3:])
    return output
