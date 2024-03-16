def delete_enclosed(input_list):
    output_list = []
    for sublist in input_list:
        new_str = ''
        inside = False
        for char in sublist[0]:
            if char == '/':
                inside = not inside
            elif not inside:
                new_str += char
        output_list.append(new_str)
    return output_list

# Test the function with the given input
input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed(input_list))
