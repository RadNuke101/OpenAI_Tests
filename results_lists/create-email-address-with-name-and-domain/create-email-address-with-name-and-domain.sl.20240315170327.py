def manipulate_input(input_list):
    output_list = []
    for input_data in input_list:
        output = input_data[0][0] + input_data[1] + '_' + input_data[2]
        output_list.append(output)
    return output_list

input_list = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(manipulate_input(input_list))
