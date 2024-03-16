def get_second_word(input_list):
    return [phrase[1] for phrase in input_list]

input_list = [['Park Kim'], ['Lee Kim'], ['Kim Lee']]
output = get_second_word(input_list)
print(output)
