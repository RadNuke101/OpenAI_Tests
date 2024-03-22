# Prompt: if there is more than two words in the inputted phrase, return everything between the first and last word
# Input: ['susan ann chang'] Output: ann
# Input: ['ayako tanaka'] Output: 
# Input: ['bobby t. smith'] Output: t.
# Input: ['anthory r. tom brown'] Output: r. tom

def get_middle_word(input_phrase):
    words = input_phrase.split()
    
    if len(words) > 2:
        return ' '.join(words[1:-1])
    else:
        return ''

# Test cases
print(get_middle_word('susan ann chang'))  # Output: ann
print(get_middle_word('ayako tanaka'))     # Output: 
print(get_middle_word('bobby t. smith'))    # Output: t.
print(get_middle_word('anthory r. tom brown'))  # Output: r. tom
