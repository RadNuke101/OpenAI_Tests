def format_phone_numbers(phone_numbers):
    formatted_numbers = []
    for number in phone_numbers:
        formatted_number = '(' + number[0][:3] + ') ' + number[0][4:]
        formatted_numbers.append(formatted_number)
    return formatted_numbers

input_numbers = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094'], ['830-941-991']]
output_numbers = format_phone_numbers(input_numbers)
print(output_numbers)
