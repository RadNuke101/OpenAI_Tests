def process_input(input_list):
    output_list = []
    for phrase_list in input_list:
        phrase = phrase_list[0]
        words = phrase.split()
        if len(words) > 1:
            output_list.append(words[0])
        else:
            output_list.append('')
    return output_list

input_list = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output = process_input(input_list)
print(output)
