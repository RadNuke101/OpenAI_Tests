def extract_numbers(data):
    return [num for sublist in data for num in sublist[0].split('-')[1:]]

input_data = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
output_data = ['242', '916', '599', '424', '980', '655']

assert extract_numbers(input_data) == output_data
