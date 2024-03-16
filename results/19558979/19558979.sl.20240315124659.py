def get_letter_at_position(expression, position):
    return expression[int(position) - 1]

def get_letters(input_list):
    return [get_letter_at_position(expression, position) for expression, position in input_list]

input_list = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
output = get_letters(input_list)
print(output)
