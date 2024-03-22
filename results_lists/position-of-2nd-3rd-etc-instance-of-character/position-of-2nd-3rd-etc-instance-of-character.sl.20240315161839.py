def find_positions(inputs):
    output = []
    for inp in inputs:
        first_instance = inp[0].find(inp[1])
        second_instance = inp[0].find(inp[1], first_instance + 1)
        third_instance = inp[0].find(inp[1], second_instance + 1)
        output.append(str(first_instance))
        output.append(str(third_instance))
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
