def delete_enclosed_text(input_list):
    output_list = []
    for sublist in input_list:
        new_sublist = []
        for item in sublist:
            while '/' in item:
                start_index = item.index('/')
                end_index = item.index('/', start_index + 1)
                item = item[:start_index] + item[end_index + 1:]
            new_sublist.append(item)
        output_list.append(' '.join(new_sublist))
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed_text(input_list))
