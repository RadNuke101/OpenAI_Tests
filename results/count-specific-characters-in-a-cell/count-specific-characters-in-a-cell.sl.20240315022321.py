def count_letter_occurrences(inputs):
    output = []
    for input_pair in inputs:
        text = input_pair[0]
        letter = input_pair[1]
        count = text.count(letter)
        output.append(str(count))
    return output

inputs = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(inputs))
