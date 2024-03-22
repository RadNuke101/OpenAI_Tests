def count_occurrences(input_list):
    output = []
    for pair in input_list:
        expression = pair[0]
        phrase = pair[1]
        count = expression.count(phrase)
        output.append(count)
    return output

input_list = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_occurrences(input_list))
