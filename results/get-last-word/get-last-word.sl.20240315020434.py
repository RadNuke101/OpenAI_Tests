def return_last_word(input_list):
    return [phrase[0].split()[-1] for phrase in input_list]

input_list = [['focus on one thing at a time'], ['premature opt is the root of all evil'], ['where is life']]
output = return_last_word(input_list)
print(output)
