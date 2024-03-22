def manipulate_input(input_list):
    output_list = []
    for input_item in input_list:
        first_letter = input_item[0][0]
        new_string = first_letter + input_item[1] + "_" + input_item[2]
        output_list.append(new_string)
    return output_list

input_list = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
output = manipulate_input(input_list)
print(output)
