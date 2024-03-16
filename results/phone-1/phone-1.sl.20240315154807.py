def extract_numbers(data):
    return [x.split('-')[1] for sublist in data for x in sublist]

input_data = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
output_data = extract_numbers(input_data)
print(output_data)
