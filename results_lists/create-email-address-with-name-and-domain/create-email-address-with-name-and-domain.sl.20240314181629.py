def generate_output(input_list):
    output_list = []
    for input_data in input_list:
        first_letter = input_data[0][0]
        new_string = first_letter + input_data[1] + "_" + input_data[2]
        output_list.append(new_string)
    return output_list

input_list = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
output = generate_output(input_list)
print(output)
