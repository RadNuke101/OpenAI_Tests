def find_positions(inputs):
    output = []
    for inp in inputs:
        first_input = inp[0]
        second_input = inp[1]
        third_input = inp[2]

        first_position = first_input.find(second_input)
        second_position = first_input.find(second_input, first_position + 1)
        third_position = first_input.find(second_input, second_position + 1)

        output.append(str(first_position + 1))
        output.append(str(third_position + 1))

    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
