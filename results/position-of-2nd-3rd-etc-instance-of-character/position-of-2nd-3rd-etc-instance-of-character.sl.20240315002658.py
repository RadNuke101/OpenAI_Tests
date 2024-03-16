def find_positions(inputs):
    output = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        count = int(item[2])
        
        positions = [i for i, char in enumerate(first_input) if char == second_input]
        if len(positions) >= count:
            output.extend([str(positions[count-1]+1), str(positions[count*2-1]+1)])
        else:
            output.extend(['-1', '-1'])
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
