def find_matching_phrase(input_list):
    for phrases in input_list:
        if phrases[2] in phrases[0]:
            return phrases[0]
        elif phrases[2] in phrases[1]:
            return phrases[1]

input_list = [['I love apples', 'I hate bananas', 'banana'], ['I love apples', 'I hate bananas', 'apple']]
output = [find_matching_phrase(input_list[0]), find_matching_phrase(input_list[1])]
print(output)
