def return_last_word(phrases):
    return [phrase[0].split()[-1] for phrase in phrases]

input_phrases = [['focus on one thing at a time'], ['premature opt is the root of all evil'], ['where is life']]
output_last_words = return_last_word(input_phrases)
print(output_last_words)
