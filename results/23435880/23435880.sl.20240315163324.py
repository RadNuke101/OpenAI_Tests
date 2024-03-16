def count_word_appearances(input_list):
    output = []
    for pair in input_list:
        expression, word = pair[0], pair[1]
        count = expression.count(word)
        output.append(str(count))
    return output

input_list = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
print(count_word_appearances(input_list))
