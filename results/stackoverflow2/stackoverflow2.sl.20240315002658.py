def remove_last_word(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        new_item = ' '.join(words[:-1])
        output.append(new_item)
    return output

input_list = [['india china japan'], ['indonesia korea']]
print(remove_last_word(input_list))
