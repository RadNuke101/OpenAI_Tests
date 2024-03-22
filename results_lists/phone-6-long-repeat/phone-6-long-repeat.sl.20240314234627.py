def extract_numbers(input_list):
    output = []
    for item in input_list:
        number = item[0].split(' ')[1]
        output.append(number)
    return output
