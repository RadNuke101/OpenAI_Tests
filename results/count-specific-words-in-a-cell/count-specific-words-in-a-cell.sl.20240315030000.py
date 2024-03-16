def count_occurrences(inputs):
    output = []
    for input_pair in inputs:
        expression = input_pair[0]
        phrase = input_pair[1]
        count = expression.count(phrase)
        output.append(str(count))
    return output

inputs = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_occurrences(inputs))
