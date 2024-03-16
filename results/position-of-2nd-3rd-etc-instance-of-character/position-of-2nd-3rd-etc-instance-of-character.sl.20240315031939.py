def find_positions(inputs):
    output = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        third_input = item[2]
        
        first_position = first_input.find(second_input)
        second_position = first_input.find(second_input, first_position + 1)
        third_position = first_input.find(second_input, second_position + 1)
        
        output.append(str(first_position))
        output.append(str(third_position))
    
    return output

# Test the function with the provided input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
