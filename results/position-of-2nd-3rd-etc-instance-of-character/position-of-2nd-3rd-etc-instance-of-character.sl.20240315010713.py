def find_positions(inputs):
    positions = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        instance_num = int(item[2])
        
        count = 0
        for i, char in enumerate(first_input):
            if char == second_input:
                count += 1
                if count == instance_num:
                    positions.append(str(i+1))
                    break
    
    return positions

# Test the function with the provided input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
output = find_positions(inputs)
print(output)
