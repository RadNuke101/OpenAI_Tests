def count_characters(expressions):
    result = []
    for exp in expressions:
        char_count = sum(len(word) for word in exp)
        result.append(str(char_count))
    return result

input_data = [['The'], ['The quick fox'], ['The quick  fox']]
output_data = count_characters(input_data)
print(output_data)
