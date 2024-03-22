def find_matching_phrase(phrases, word):
    for phrase in phrases:
        if word in phrase[2]:
            return [phrase[0], phrase[1]]

input_data = [['I love apples', 'I hate bananas', 'banana'], ['I love apples', 'I hate bananas', 'apple']]
output = [find_matching_phrase(input_data, 'banana'), find_matching_phrase(input_data, 'apple')]
print(output)
