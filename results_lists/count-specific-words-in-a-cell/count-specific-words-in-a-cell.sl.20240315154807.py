def count_appearance(input_list):
    output = []
    for pair in input_list:
        count = pair[0].count(pair[1])
        output.append(str(count))
    return output

input_list = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_appearance(input_list))
