def get_second_word(phrases):
    return [phrase[1] for phrase in phrases]

input_phrases = [['Park Kim'], ['Lee Kim'], ['Kim Lee']]
output_words = get_second_word(input_phrases)
print(output_words)
