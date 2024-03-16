def find_positions(inputs):
    positions = []
    
    for item in inputs:
        string = item[0]
        target = item[1]
        instance = int(item[2])
        
        count = 0
        for i, char in enumerate(string):
            if char == target:
                count += 1
                if count == instance:
                    positions.append(str(i+1))
                    break
    
    return positions

# Test the function with the provided input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
output = find_positions(inputs)
print(output)
