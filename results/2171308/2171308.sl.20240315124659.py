def process_names(input_list):
    output_list = []
    for names in input_list:
        first_word = names[0].split()[0]
        last_name = names[0].split()[1]
        output_list.append(first_word[0] + ' ' + last_name)
    return output_list

input_list = [['John Doe'], ['Mayur Naik'], ['Nimit Singh']]
print(process_names(input_list))
