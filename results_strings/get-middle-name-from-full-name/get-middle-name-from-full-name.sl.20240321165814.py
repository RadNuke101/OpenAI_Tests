# Prompt: if there is more than two words in the inputted phrase, return everything between the first and last word
# Input: ['susan ann chang'], Output: 'ann'
# Input: ['ayako tanaka'], Output: ''
# Input: ['bobby t. smith'], Output: 't.'
# Input: ['anthory r. tom brown'], Output: 'r. tom'

def return_between_first_and_last(input_str):
    words = input_str.split()
    if len(words) > 2:
        return ' '.join(words[1:-1])
    else:
        return ''

# Test cases
print(return_between_first_and_last('susan ann chang'))  # Output: 'ann'
print(return_between_first_and_last('ayako tanaka'))  # Output: ''
print(return_between_first_and_last('bobby t. smith'))  # Output: 't.'
print(return_between_first_and_last('anthory r. tom brown'))  # Output: 'r. tom'
