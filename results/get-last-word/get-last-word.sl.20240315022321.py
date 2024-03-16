def return_last_word(input_list):
    output_list = []
    for phrase in input_list:
        last_word = phrase[0].split()[-1]
        output_list.append(last_word)
    return output_list

input_list = [['focus on one thing at a time'], ['premature opt is the root of all evil'], ['where is life']]
output = return_last_word(input_list)
print(output)
