def return_last_three_numbers(input_list):
    output = []
    for sublist in input_list:
        last_three = sublist[0][-3:]
        output.append(last_three)
    return output
