def process_inputs(inputs):
    result = []
    for input_list in inputs:
        first_letter = input_list[0][0]
        new_string = first_letter + input_list[1] + "_" + input_list[2]
        result.append(new_string)
    return result

inputs = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
output = process_inputs(inputs)
print(output)
