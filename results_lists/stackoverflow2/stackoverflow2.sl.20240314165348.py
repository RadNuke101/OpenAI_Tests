def remove_last_word(input_list):
    output_list = []
    for item in input_list:
        output_list.append(' '.join(item[0].split()[:-1]))
    return output_list

input_list = [['india china japan'], ['indonesia korea']]
output = remove_last_word(input_list)
print(output)
