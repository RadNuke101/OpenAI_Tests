def find_phrase_starting_with_underscore(input_str):
    phrases = input_str.split()
    for phrase in phrases:
        if phrase.startswith('_'):
            return phrase

# Prompt: return the first phrase in the inputted expression that begins with "_"
# Input: ['this is a _username in the middle']
# Output: _username
print(find_phrase_starting_with_underscore('this is a _username in the middle'))

# Input: ['twitter names look like= _name']
# Output: _name
print(find_phrase_starting_with_underscore('twitter names look like= _name'))

# Input: ['with two _name1 and _name2']
# Output: _name1
print(find_phrase_starting_with_underscore('with two _name1 and _name2'))
