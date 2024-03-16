def delete_enclosed(input_list):
    output = []
    for item in input_list:
        new_item = item[0]
        start_index = new_item.find('/')
        while start_index != -1:
            end_index = new_item.find('/', start_index + 1)
            if end_index != -1:
                new_item = new_item[:start_index] + new_item[end_index + 1:]
            start_index = new_item.find('/', start_index)
        output.append(new_item)
    return output

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
