def extract_numbers(input_list):
    output = []
    for sublist in input_list:
        for item in sublist:
            numbers = item.split('-')
            output.append(numbers[1])
    return output
