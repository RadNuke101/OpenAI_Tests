def count_occurrences(input_list):
    result = []
    for item in input_list:
        count = item[0].count(item[1])
        result.append(str(count))
    return result

input_list = [['The fox jumped over the fox', 'fox'], ['The fox jumped over the fox', 'ox'], ['The fox jumped over the fox', 'Fox']]
output = count_occurrences(input_list)
print(output)
