def count_characters(input_list):
    output_list = []
    for words in input_list:
        count = 0
        for word in words:
            count += len(word)
        output_list.append(str(count))
    return output_list

input_list = [['The'], ['The quick fox'], ['The quick  fox']]
print(count_characters(input_list))
