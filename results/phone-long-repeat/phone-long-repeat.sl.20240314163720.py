def return_first_three_numbers(input_list):
    output = []
    for sublist in input_list:
        output.append(sublist[0][:3])
    return output
