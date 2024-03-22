def process_inputs(inputs):
    output = []
    for input_list in inputs:
        first_letter = input_list[0][0]
        new_string = first_letter + input_list[1] + "_" + input_list[2]
        output.append(new_string)
    return output

inputs = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(process_inputs(inputs))
