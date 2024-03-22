def count_occurrences(input_list):
    output = []
    for item in input_list:
        count = item[0].count(item[1])
        output.append(str(count))
    return output

input_list = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
print(count_occurrences(input_list))
