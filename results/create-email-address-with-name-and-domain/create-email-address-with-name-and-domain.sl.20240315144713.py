def generate_output(input_list):
    output = []
    for input_data in input_list:
        first_letter = input_data[0][0]
        new_string = first_letter + input_data[1] + "_" + input_data[2]
        output.append(new_string)
    return output

input_list = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(generate_output(input_list))
