# Prompt: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column)
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas

def find_phrase(input1, input2, word):
    if word in input1:
        return input1
    elif word in input2:
        return input2

# Test cases
input1 = 'I love apples'
input2 = 'I hate bananas'
word = 'banana'
print(find_phrase(input1, input2, word))  # Output: I hate bananas

input1 = 'I love apples'
input2 = 'I hate bananas'
word = 'apple'
print(find_phrase(input1, input2, word))  # Output: I love apples
