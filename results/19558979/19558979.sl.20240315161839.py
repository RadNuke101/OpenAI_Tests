def get_letter_at_position(expression, position):
    return expression[int(position) - 1]

def get_letters_at_positions(inputs):
    return [get_letter_at_position(expression, position) for expression, position in inputs]

inputs = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
output = get_letters_at_positions(inputs)
print(output)
