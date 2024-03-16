def process_input(input_data):
    output = []
    for phrase in input_data:
        if len(phrase[0].split()) > 1:
            output.append(phrase[0].split()[0])
        else:
            output.append('')
    return output

input_data = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output = process_input(input_data)
print(output)
