def find_matching_phrase(input_list):
    output = []
    for phrases in input_list:
        for phrase in phrases[:2]:
            if phrases[2] in phrase:
                output.append(phrase)
    return output

input_list = [['I love apples', 'I hate bananas', 'banana'], ['I love apples', 'I hate bananas', 'apple']]
print(find_matching_phrase(input_list))
