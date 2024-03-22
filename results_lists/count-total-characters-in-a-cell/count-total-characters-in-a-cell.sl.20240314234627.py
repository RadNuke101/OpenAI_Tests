def count_characters(expressions):
    output = []
    for exp in expressions:
        count = sum(len(word) for word in exp)
        output.append(str(count))
    return output

input_data = [['The'], ['The quick fox'], ['The quick  fox']]
output_data = count_characters(input_data)
print(output_data)
