def delete_enclosed_text(input_list):
    output = []
    for item in input_list:
        new_item = item[0]
        while '/' in new_item:
            start_index = new_item.index('/')
            end_index = new_item.index('/', start_index + 1)
            new_item = new_item[:start_index] + new_item[end_index + 1:]
        output.append(new_item)
    return output

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed_text(input_list))
