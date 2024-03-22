def process_input(input_list):
    output = []
    for phrase in input_list:
        if len(phrase[0].split()) > 1:
            output.append(phrase[0].split()[0])
        else:
            output.append('')
    return output

input_list = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output = process_input(input_list)
print(output)
