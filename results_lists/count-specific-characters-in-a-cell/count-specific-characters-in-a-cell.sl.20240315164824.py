def count_letter_occurrences(inputs):
    def count_occurrences(expression, letter):
        return expression.count(letter)

    outputs = []
    for expression, letter in inputs:
        outputs.append(str(count_occurrences(expression, letter)))

    return outputs

inputs = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(inputs))
