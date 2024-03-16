def extract_words(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        if len(words) > 2:
            output.append(' '.join(words[1:-1]))
        else:
            output.append('')
    return output

input_list = [['susan ann chang'], ['ayako tanaka'], ['bobby t. smith'], ['anthory r. tom brown']]
print(extract_words(input_list))
