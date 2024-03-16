def remove_spaces(input_list):
    output_list = []
    for item in input_list:
        cleaned_item = item[0].strip()
        output_list.append(cleaned_item)
    return output_list

input_list = [['  The shawshank'], ['The    godfather'], ['    pulp   fiction']]
output = remove_spaces(input_list)
print(output)
