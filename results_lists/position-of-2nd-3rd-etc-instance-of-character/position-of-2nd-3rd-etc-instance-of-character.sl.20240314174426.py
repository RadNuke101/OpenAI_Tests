def find_positions(inputs):
    output = []
    for lst in inputs:
        first_input = lst[0]
        second_input = lst[1]
        count = 0
        positions = []
        for i, char in enumerate(first_input):
            if char == second_input:
                count += 1
                if count == 1 or count == 3:
                    positions.append(str(i+1))
        output.append(positions)
    return [' '.join(position) for position in output]

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
