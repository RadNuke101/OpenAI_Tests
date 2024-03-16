def return_first_three_numbers(input_list):
    output = []
    for sublist in input_list:
        output.append(sublist[0][1:4])
    return output
