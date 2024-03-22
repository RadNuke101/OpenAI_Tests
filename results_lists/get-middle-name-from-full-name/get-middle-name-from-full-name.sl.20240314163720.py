def extract_words(input_list):
    output_list = []
    for sublist in input_list:
        if len(sublist[0].split()) > 2:
            words = sublist[0].split()[1:-1]
            output_list.append(' '.join(words))
        else:
            output_list.append('')
    return output_list

input_list = [['susan ann chang'], ['ayako tanaka'], ['bobby t. smith'], ['anthory r. tom brown']]
print(extract_words(input_list))
