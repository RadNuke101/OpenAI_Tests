# Prompt: return the first phrase in the inputted expression that begins with "_"
# Input: ['this is a _username in the middle']
# Output: _username

def find_phrase_with_underscore(input_str):
    words = input_str.split()
    for word in words:
        if word.startswith('_'):
            return word

# Test cases
print(find_phrase_with_underscore('this is a _username in the middle'))  # Output: _username
print(find_phrase_with_underscore('twitter names look like= _name'))  # Output: _name
print(find_phrase_with_underscore('with two _name1 and _name2'))  # Output: _name1
