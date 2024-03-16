def process_input(input_list):
    output_list = []
    for phrase in input_list:
        if len(phrase[0].split()) > 1:
            output_list.append(phrase[0].split()[0])
        else:
            output_list.append('')
    return output_list

input_list = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output = process_input(input_list)
print(output)
