def return_last_three_numbers(input_list):
    output = []
    for sublist in input_list:
        number = sublist[0][-3:]
        output.append(number)
    return output
