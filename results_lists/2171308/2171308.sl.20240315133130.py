def format_names(input_list):
    output_list = []
    for names in input_list:
        first_name = names[0].split()[0]
        last_name = names[0].split()[1]
        output_list.append(f'{first_name[0]} {last_name}')
    return output_list

input_list = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
print(format_names(input_list))
