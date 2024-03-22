def find_positions(inputs):
    output = []
    for lst in inputs:
        first_input = lst[0]
        second_input = lst[1]
        third_input = lst[2]
        
        first_position = first_input.find(second_input)
        second_position = first_input.find(second_input, first_position + 1)
        third_position = first_input.find(second_input, second_position + 1)
        
        output.append(str(first_position))
        output.append(str(third_position))
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
