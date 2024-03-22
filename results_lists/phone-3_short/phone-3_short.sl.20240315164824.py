def format_phone_numbers(input):
    output = []
    for item in input:
        phone_number = item[0]
        formatted_number = "(" + phone_number[:3] + ") " + phone_number[4:]
        output.append(formatted_number)
    return output

input = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094'], ['830-941-991']]
output = format_phone_numbers(input)
print(output)
