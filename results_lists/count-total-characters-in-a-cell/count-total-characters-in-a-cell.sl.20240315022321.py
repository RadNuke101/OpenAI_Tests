def count_characters(input_list):
    output = []
    for item in input_list:
        count = sum(len(word) for word in item)
        output.append(str(count))
    return output

input_list = [['The'], ['The quick fox'], ['The quick  fox']]
print(count_characters(input_list))
