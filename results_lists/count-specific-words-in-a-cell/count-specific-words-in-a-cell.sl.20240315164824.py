def count_occurrences(inputs):
    output = []
    for inp in inputs:
        count = inp[0].count(inp[1])
        output.append(str(count))
    return output

inputs = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_occurrences(inputs))
