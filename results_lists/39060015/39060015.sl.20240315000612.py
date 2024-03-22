def delete_enclosed(input_list):
    output_list = []
    for item in input_list:
        new_item = item[0].replace('/', '').strip()
        output_list.append(new_item)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
