def extract_numbers(input_list):
    output = []
    for item in input_list:
        numbers = item[0].split('-')
        output.extend([numbers[1], numbers[1], numbers[1]])
    return output
