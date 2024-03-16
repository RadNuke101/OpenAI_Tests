def process_input(input_list):
    output_list = []
    for sublist in input_list:
        if len(sublist[0].split()) > 1:
            output_list.append(sublist[0].split()[0])
        else:
            output_list.append('')
    return output_list

input_list = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output = process_input(input_list)
print(output)
