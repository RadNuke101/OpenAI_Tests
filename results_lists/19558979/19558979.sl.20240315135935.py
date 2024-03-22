def get_letter_at_position(data):
    result = []
    for item in data:
        expression = item[0]
        position = int(item[1])
        result.append(expression[position - 1])
    return result

input_data = [['spreadsheet', '1'], ['spreadsheet', '2'], ['spreadsheet', '3'], ['spreadsheet', '4'], ['spreadsheet', '5']]
output = get_letter_at_position(input_data)
print(output)
