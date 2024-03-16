def find_positions(inputs):
    output = []
    for input_list in inputs:
        first_input = input_list[0]
        second_input = input_list[1]
        third_input = input_list[2]
        
        first_instance = first_input.find(second_input)
        second_instance = first_input.find(second_input, first_instance + 1)
        third_instance = first_input.find(second_input, second_instance + 1)
        
        output.append(str(first_instance))
        output.append(str(third_instance))
    
    return output

# Test the function with the provided input
inputs = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(inputs))
