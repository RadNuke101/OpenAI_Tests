def delete_enclosed(input_list):
    output = []
    for item in input_list:
        new_item = item[0].replace('/' + item[0][item[0].find('/')+1:item[0].rfind('/')+1], '')
        output.append(new_item)
    return output

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
