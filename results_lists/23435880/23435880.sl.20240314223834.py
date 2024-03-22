def count_word_occurrences(input_list):
    result = []
    for item in input_list:
        expression, word = item[0], item[1]
        result.append(str(expression.count(word)))
    return result

input_list = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
output = count_word_occurrences(input_list)
print(output)
