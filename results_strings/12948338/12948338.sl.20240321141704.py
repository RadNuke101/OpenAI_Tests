# Prompt: return count of the phrase (second column) in expression (first column)
# Input: 'An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'
# Output: 2
def count_phrase_in_expression(expression, phrase):
    count = 0
    words = expression.split()
    for word in words:
        if phrase in word:
            count += 1
    return count

# Test the function with the provided inputs
input1 = 'An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'
output1 = count_phrase_in_expression(input1[0], input1[1])
print(output1)  # Output should be 2

input2 = 'An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'
output2 = count_phrase_in_expression(input2[0], input2[1])
print(output2)  # Output should be 1

input3 = 'An _example string with _example in it is awesome _example', 'example'
output3 = count_phrase_in_expression(input3[0], input3[1])
print(output3)  # Output should be 3
