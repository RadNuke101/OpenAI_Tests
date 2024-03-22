def count_characters(expressions):
    result = []
    for exp in expressions:
        count = sum(len(word) for word in exp)
        result.append(str(count))
    return result

input_data = [['The'], ['The quick fox'], ['The quick  fox']]
output_data = count_characters(input_data)
print(output_data)
