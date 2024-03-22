def manipulate_inputs(inputs):
    outputs = []
    for input_list in inputs:
        first_letter = input_list[0][0]
        new_string = first_letter + input_list[1] + "_" + input_list[2]
        outputs.append(new_string)
    return outputs

# Test the function with the given input
inputs = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(manipulate_inputs(inputs))
