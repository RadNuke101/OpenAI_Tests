def count_word_occurrences(data):
    result = []
    for item in data:
        expression, word = item[0], item[1]
        result.append(str(expression.count(word)))
    return result

input_data = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
output = count_word_occurrences(input_data)
print(output)
