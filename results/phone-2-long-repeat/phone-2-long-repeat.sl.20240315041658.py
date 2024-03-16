def return_last_three_numbers(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(sublist[0][-3:])
    return output_list
