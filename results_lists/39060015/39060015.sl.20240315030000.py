def delete_enclosed_words(input_list):
    output_list = []
    for sublist in input_list:
        new_string = ''
        inside_slash = False
        for char in sublist[0]:
            if char == '/':
                inside_slash = not inside_slash
            elif not inside_slash:
                new_string += char
        output_list.append(new_string)
    return output_list

input_list = [['This is a line. /delete words in the area /keep this part'], ['/delete words in the area /']]
print(delete_enclosed_words(input_list))
