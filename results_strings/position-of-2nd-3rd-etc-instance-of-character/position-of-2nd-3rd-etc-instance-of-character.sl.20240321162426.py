# Prompt: return the position of the first and third instance of the second input in the first input
# Input: '100x15x50', 'x', '2'
# Output: 7

def find_positions(input_str, char, occurrence):
    count = 0
    positions = []
    
    for i in range(len(input_str)):
        if input_str[i] == char:
            count += 1
            if count == int(occurrence):
                positions.append(i+1)
    
    return positions[0] if len(positions) > 0 else -1

# Test cases
print(find_positions('100x15x50', 'x', '2'))  # Output: 7
print(find_positions('cat-in-the-hat', '-', '3'))  # Output: 11
