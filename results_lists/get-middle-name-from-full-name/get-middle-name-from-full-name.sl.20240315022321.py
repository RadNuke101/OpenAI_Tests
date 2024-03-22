def extract_words(input_list):
    output_list = []
    for item in input_list:
        words = item[0].split()
        if len(words) > 2:
            output_list.append(' '.join(words[1:-1]))
        else:
            output_list.append('')
    return output_list

input_list = [['susan ann chang'], ['ayako tanaka'], ['bobby t. smith'], ['anthory r. tom brown']]
print(extract_words(input_list))
