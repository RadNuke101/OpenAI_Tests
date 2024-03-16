def count_appearances(inputs):
    output = []
    for input_pair in inputs:
        count = input_pair[0].count(input_pair[1])
        output.append(str(count))
    return output

inputs = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_appearances(inputs))
