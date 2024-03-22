def count_phrase_appearance(inputs):
    output = []
    for pair in inputs:
        count = pair[0].count(pair[1])
        output.append(str(count))
    return output

# Test the function with the given input
inputs = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_phrase_appearance(inputs))
