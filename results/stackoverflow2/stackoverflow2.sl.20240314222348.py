def remove_last_word(input_list):
    output = []
    for sublist in input_list:
        output.append(' '.join(sublist[0].split()[:-1]))
    return output

input_list = [['india china japan'], ['indonesia korea']]
print(remove_last_word(input_list))
