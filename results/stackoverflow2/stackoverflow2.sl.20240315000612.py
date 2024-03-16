def remove_last_word(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        output.append(' '.join(words[:-1]))
    return output

input_list = [['india china japan'], ['indonesia korea']]
print(remove_last_word(input_list))
