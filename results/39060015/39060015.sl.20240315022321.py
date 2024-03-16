def delete_enclosed(input_list):
    output_list = []
    for sublist in input_list:
        new_sublist = sublist[0]
        while '/' in new_sublist:
            start_index = new_sublist.find('/')
            end_index = new_sublist.find('/', start_index + 1)
            if end_index != -1:
                new_sublist = new_sublist[:start_index] + new_sublist[end_index + 1:]
            else:
                new_sublist = new_sublist[:start_index]
        output_list.append(new_sublist)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
