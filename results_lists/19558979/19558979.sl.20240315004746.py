def get_letter_at_position(input_list):
    output = []
    for item in input_list:
        expression = item[0]
        position = int(item[1]) - 1
        output.append(expression[position])
    return output

input_list = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
print(get_letter_at_position(input_list))
