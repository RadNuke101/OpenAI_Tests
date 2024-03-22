def find_positions(input_str, char, instance):
    count = 0
    positions = []
    
    for i in range(len(input_str)):
        if input_str[i] == char:
            count += 1
            if count == int(instance):
                positions.append(i)
    
    if len(positions) >= int(instance):
        return positions[int(instance)-1]
    else:
        return -1

# Prompt: return the position of the first and third instance of the second input in the first input
# Input: ['100x15x50', 'x', '2']
# Output: 7
print(find_positions('100x15x50', 'x', '2'))  # Output: 7

# Prompt: return the position of the first and third instance of the second input in the first input
# Input: ['cat-in-the-hat', '-', '3']
# Output: 11
print(find_positions('cat-in-the-hat', '-', '3'))  # Output: 11
