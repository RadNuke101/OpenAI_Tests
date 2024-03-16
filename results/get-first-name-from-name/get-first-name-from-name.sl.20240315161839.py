def get_first_word(phrases):
    return [phrase[0].split()[0] for phrase in phrases]

input_phrases = [['Susan Ann Chang'], ['Ayako Tanaka'], ['Bobby T. smth']]
output_words = get_first_word(input_phrases)
print(output_words)
