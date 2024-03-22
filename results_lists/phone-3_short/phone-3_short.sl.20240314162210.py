def format_phone_numbers(input_list):
    output_list = []
    for phone_number in input_list:
        formatted_number = '(' + phone_number[0][:3] + ') ' + phone_number[0][4:]
        output_list.append(formatted_number)
    return output_list

input_list = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094'], ['830-941-991']]
output = format_phone_numbers(input_list)
print(output)
