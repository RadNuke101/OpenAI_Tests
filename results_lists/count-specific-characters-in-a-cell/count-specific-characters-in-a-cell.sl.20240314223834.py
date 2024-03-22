def count_letter_occurrences(inputs):
    output = []
    for expression, letter in inputs:
        count = expression.count(letter)
        output.append(str(count))
    return output

inputs = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(inputs))
