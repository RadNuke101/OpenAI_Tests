# Prompt: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column)
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas
# Input: ['I love apples', 'I hate bananas', 'apple']
# Output: I love apples

def find_phrase(input1, input2, word):
    if word in input1:
        return input1
    elif word in input2:
        return input2

input1 = 'I love apples'
input2 = 'I hate bananas'
word = 'banana'
output = find_phrase(input1, input2, word)
print(output)
