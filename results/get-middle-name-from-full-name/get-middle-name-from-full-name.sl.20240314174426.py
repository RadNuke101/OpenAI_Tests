def extract_words(input_list):
    output_list = []
    for words in input_list:
        if len(words[0].split()) > 2:
            output_list.append(' '.join(words[0].split()[1:-1]))
        else:
            output_list.append('')
    return output_list

input_list = [['susan ann chang'], ['ayako tanaka'], ['bobby t. smith'], ['anthory r. tom brown']]
output = extract_words(input_list)
print(output)
