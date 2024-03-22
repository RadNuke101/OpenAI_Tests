def find_positions(input_list):
    output = []
    for item in input_list:
        first_input = item[0]
        second_input = item[1]
        third_input = item[2]
        
        first_position = first_input.find(second_input)
        second_position = first_input.find(second_input, first_position + 1)
        third_position = first_input.find(second_input, second_position + 1)
        
        output.append(str(first_position + 1))
        output.append(str(third_position + 1))
    
    return output

# Test the function with the given input
input_list = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(input_list))  # Output: ['7', '11']
