def find_phrase(input_list):
    output = []
    for phrases in input_list:
        if phrases[2] in phrases[0]:
            output.append(phrases[0])
        else:
            output.append(phrases[1])
    return output

input_list = [['I love apples', 'I hate bananas', 'banana'], ['I love apples', 'I hate bananas', 'apple']]
print(find_phrase(input_list))
