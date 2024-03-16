def find_matching_phrase(phrases):
    for phrase in phrases:
        if phrase[2] in phrase[0]:
            return phrase[0]
        elif phrase[2] in phrase[1]:
            return phrase[1]

input_phrases = [['I love apples', 'I hate bananas', 'banana'], ['I love apples', 'I hate bananas', 'apple']]
output = [find_matching_phrase(phrase) for phrase in input_phrases]
print(output)
