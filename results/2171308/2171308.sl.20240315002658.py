def process_names(input_list):
    output_list = []
    for name in input_list:
        first_name = name[0].split()[0]
        last_name = name[0].split()[1]
        output_list.append(f"{first_name[0]} {last_name}")
    return output_list

input_list = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
output = process_names(input_list)
print(output)
