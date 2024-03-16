def delete_elements(input_list):
    output = []
    for item in input_list:
        output.append(item[0][int(item[1]):])
    return output

input_list = [['1234', '1'], ['**512A', '2'], ['343DMX', '3']]
print(delete_elements(input_list))
