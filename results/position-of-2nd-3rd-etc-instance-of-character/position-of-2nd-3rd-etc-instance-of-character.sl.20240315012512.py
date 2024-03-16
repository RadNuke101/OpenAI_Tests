def find_positions(input_list):
    output = []
    for item in input_list:
        first_input = item[0]
        second_input = item[1]
        third_instance = int(item[2])
        
        first_instance = first_input.find(second_input)
        second_instance = first_input.find(second_input, first_instance + 1)
        third_instance_pos = first_input.find(second_input, second_instance + 1)
        
        output.append(str(first_instance + 1))
        output.append(str(third_instance_pos + 1))
    
    return output

input_list = [['100x15x50', 'x', '2'], ['cat-in-the-hat', '-', '3']]
print(find_positions(input_list))
