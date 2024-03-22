def find_positions(inputs):
    output = []
    for item in inputs:
        first_input = item[0]
        second_input = item[1]
        third_input = item[2]
        
        first_instance = first_input.find(second_input)
        second_instance = first_input.find(second_input, first_instance + 1)
        third_instance = first_input.find(second_input, second_instance + 1)
        
        output.append(str(first_instance + 1))
        output.append(str(third_instance + 1))
    
    return output

# Test the function with the given input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
