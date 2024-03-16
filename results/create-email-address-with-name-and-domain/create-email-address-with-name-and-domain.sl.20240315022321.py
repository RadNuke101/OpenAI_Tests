def manipulate_input(input_list):
    output_list = []
    for item in input_list:
        first_letter = item[0][0]
        new_string = first_letter + item[1] + "_" + item[2]
        output_list.append(new_string)
    return output_list

input_list = [['ayako', 'ogawa', 'acme.com'], ['amy', 'johnson', 'google.com'], ['tom', 'chang', 'upenn.edu']]
print(manipulate_input(input_list))
