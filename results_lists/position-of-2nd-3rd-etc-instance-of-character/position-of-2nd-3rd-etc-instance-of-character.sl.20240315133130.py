def find_positions(inputs):
    positions = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        instance = int(item[2])
        
        count = 0
        for i in range(len(first_input)):
            if first_input[i] == second_input:
                count += 1
                if count == instance:
                    positions.append(str(i))
                    break
    
    return positions

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
output = find_positions(inputs)
print(output)
