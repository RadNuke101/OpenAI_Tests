def count_word_appearance(input_data):
    output = []
    for item in input_data:
        expression, word = item[0], item[1]
        count = expression.count(word)
        output.append(str(count))
    return output

input_data = [['apple apples', 'apple'], ['an orange among the oranges is a spoiled orange', 'orange']]
print(count_word_appearance(input_data))
