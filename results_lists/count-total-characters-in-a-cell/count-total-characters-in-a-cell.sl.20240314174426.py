def count_characters(expressions):
    result = []
    for expression in expressions:
        count = sum(len(word) for word in expression)
        result.append(str(count))
    return result

input_expressions = [['The'], ['The quick fox'], ['The quick  fox']]
output_counts = count_characters(input_expressions)
print(output_counts)
