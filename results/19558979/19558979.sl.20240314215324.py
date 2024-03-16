def get_letter_at_position(expression, position):
    return expression[int(position) - 1]

input_data = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
output_data = [get_letter_at_position(expression, position) for expression, position in input_data]
print(output_data)
