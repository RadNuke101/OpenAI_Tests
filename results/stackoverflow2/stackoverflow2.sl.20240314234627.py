def remove_last_word(input_list):
    output_list = []
    for item in input_list:
        words = item[0].split()
        new_item = ' '.join(words[:-1])
        output_list.append(new_item)
    return output_list

input_list = [['india china japan'], ['indonesia korea']]
output = remove_last_word(input_list)
print(output)
