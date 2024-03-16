def count_word_occurrences(input_list):
    result = []
    for expression, word in input_list:
        result.append(str(expression.count(word)))
    return result

input_list = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
print(count_word_occurrences(input_list))
