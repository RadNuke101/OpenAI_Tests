def get_letter_at_position(data):
    output = []
    for item in data:
        expression = item[0]
        position = int(item[1])
        letter = expression[position - 1]
        output.append(letter)
    return output

input_data = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
output_data = get_letter_at_position(input_data)
print(output_data)
