def delete_enclosed(input_list):
    output = []
    for item in input_list:
        new_item = item[0].replace('/', '').strip()
        output.append(new_item)
    return output

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
output = delete_enclosed(input_list)
print(output)
