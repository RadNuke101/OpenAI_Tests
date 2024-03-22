def extract_first_three_numbers(input_list):
    output_list = []
    for item in input_list:
        number = item[0].split()[0][1:]
        output_list.append(number)
    return output_list
