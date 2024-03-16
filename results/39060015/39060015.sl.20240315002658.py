def delete_enclosed(input_list):
    output_list = []
    for item in input_list:
        new_item = ''
        inside_slash = False
        for char in item[0]:
            if char == '/':
                inside_slash = not inside_slash
            elif not inside_slash:
                new_item += char
        output_list.append(new_item)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
