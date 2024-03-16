def count_letter_occurrences(inputs):
    output = []
    for input_pair in inputs:
        expression = input_pair[0]
        letter = input_pair[1]
        count = expression.count(letter)
        output.append(str(count))
    return output

# Test the function with the given input
inputs = [['Hannah', 'n'], ['Hannah', 'x'], ['Hannah', 'N'], ['Hannah', 'a'], ['Hannah', 'h']]
print(count_letter_occurrences(inputs))
