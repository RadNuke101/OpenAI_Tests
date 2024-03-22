def count_characters(input_list):
    output_list = []
    for sublist in input_list:
        count = sum(len(word) for word in sublist)
        output_list.append(str(count))
    return output_list

input_list = [['The'], ['The quick fox'], ['The quick  fox']]
output = count_characters(input_list)
print(output)
