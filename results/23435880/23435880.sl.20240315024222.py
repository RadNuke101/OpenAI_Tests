def count_word_occurrences(input_list):
    output = []
    for expression, word in input_list:
        count = expression.count(word)
        output.append(str(count))
    return output

input_list = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
print(count_word_occurrences(input_list))
