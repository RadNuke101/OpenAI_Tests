def remove_last_word(input):
    output = []
    for item in input:
        output.append(' '.join(item[0].split()[:-1]))
    return output

input = [['india china japan'], ['indonesia korea']]
output = ['india china', 'indonesia']

print(remove_last_word(input))
