# Prompt: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column)
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas
# Input: ['I love apples', 'I hate bananas', 'apple']
# Output: I love apples

def find_phrase(input_list):
    phrase1, phrase2, word = input_list
    if word in phrase1:
        return phrase1
    elif word in phrase2:
        return phrase2

# Test cases
print(find_phrase(['I love apples', 'I hate bananas', 'banana']))  # Output: I hate bananas
print(find_phrase(['I love apples', 'I hate bananas', 'apple']))   # Output: I love apples
