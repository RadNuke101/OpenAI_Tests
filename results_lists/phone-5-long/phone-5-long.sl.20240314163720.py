def extract_first_three_numbers(input_list):
    output = []
    for item in input_list:
        output.append(item[0].split()[0][1:])
    return output
