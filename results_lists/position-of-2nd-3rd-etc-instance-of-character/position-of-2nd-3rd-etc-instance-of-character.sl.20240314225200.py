def find_positions(inputs):
    output = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        count = int(item[2])
        
        first_position = 0
        for i in range(count):
            first_position = first_input.find(second_input, first_position + 1)
        
        output.append(str(first_position))
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
