def count_word_occurrences(input_list):
    output = []
    for expression, word in input_list:
        output.append(str(expression.count(word)))
    return output

input_list = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
print(count_word_occurrences(input_list))
