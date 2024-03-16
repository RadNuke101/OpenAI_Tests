def remove_spaces(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].strip())
    return output_list

input_list = [['  The shawshank'], ['The    godfather'], ['    pulp   fiction']]
output = remove_spaces(input_list)
print(output)
