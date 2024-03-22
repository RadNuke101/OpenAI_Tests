# Prompt: return 1 plus the number of "/n" present in inputted expression
# Input: ['one'] Output: 1
# Input: ['one/ntwo'] Output: 2
# Input: ['one/ntwo/nthree'] Output: 3

def count_slash_n(input_str):
    return str(input_str.count("/n") + 1)

# Test cases
print(count_slash_n('one'))  # Output: 1
print(count_slash_n('one/ntwo'))  # Output: 2
print(count_slash_n('one/ntwo/nthree'))  # Output: 3
