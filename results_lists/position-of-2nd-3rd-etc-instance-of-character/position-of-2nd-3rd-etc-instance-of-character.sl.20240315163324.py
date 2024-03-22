def find_positions(inputs):
    output = []
    for inp in inputs:
        first_input = inp[0]
        second_input = inp[1]
        instance_num = int(inp[2])
        
        positions = [pos for pos, char in enumerate(first_input) if char == second_input]
        
        if len(positions) >= instance_num:
            output.append(str(positions[instance_num - 1]))
        else:
            output.append('-1')
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
