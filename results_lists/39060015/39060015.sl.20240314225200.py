def delete_enclosed_text(input_list):
    output_list = []
    for item in input_list:
        new_item = item[0]
        while '/' in new_item:
            start_index = new_item.find('/')
            end_index = new_item.find('/', start_index + 1)
            if end_index != -1:
                new_item = new_item[:start_index] + new_item[end_index + 1:]
            else:
                break
        output_list.append(new_item)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
output = delete_enclosed_text(input_list)
print(output)
