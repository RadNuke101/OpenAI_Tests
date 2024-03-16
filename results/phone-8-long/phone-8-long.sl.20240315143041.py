def return_last_three_numbers(input_data):
    output = []
    for item in input_data:
        output.append(item[0][-3:])
    return output
