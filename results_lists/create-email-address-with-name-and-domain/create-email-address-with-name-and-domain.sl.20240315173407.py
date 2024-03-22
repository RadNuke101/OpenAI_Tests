def generate_output(inputs):
    output = []
    for inp in inputs:
        first_letter = inp[0][0]
        new_string = first_letter + inp[1] + "_" + inp[2]
        output.append(new_string)
    return output

inputs = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(generate_output(inputs))
