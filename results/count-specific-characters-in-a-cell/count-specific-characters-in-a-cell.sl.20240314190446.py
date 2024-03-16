def count_letter_occurrences(inputs):
    output = []
    for input_pair in inputs:
        count = input_pair[0].count(input_pair[1])
        output.append(str(count))
    return output

inputs = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(inputs))
