def find_positions(inputs):
    output = []
    for lst in inputs:
        first_input = lst[0]
        second_input = lst[1]
        count = int(lst[2])
        
        positions = [i for i, char in enumerate(first_input) if char == second_input]
        
        if len(positions) >= count:
            output.append(str(positions[count-1] + 1))
        else:
            output.append('-1')
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
