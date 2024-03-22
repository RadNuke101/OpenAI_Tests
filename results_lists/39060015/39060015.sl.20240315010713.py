def delete_enclosed(input_list):
    output_list = []
    for sublist in input_list:
        new_sublist = ''
        for item in sublist:
            start = item.find('/')
            while start != -1:
                end = item.find('/', start + 1)
                item = item[:start] + item[end + 1:]
                start = item.find('/')
            new_sublist += item
        output_list.append(new_sublist)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
