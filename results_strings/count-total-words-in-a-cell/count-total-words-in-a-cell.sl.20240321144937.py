# Prompt: return the number of words in the inputted expression
# Input: 'humpty dumpty'
# Output: 2

def count_words(input_str):
    words = input_str.split()
    return len(words)

# Test cases
print(count_words('humpty dumpty'))  # Output: 2
print(count_words('humpty dumpty sat on a wall,'))  # Output: 6
print(count_words('couldnt put humpty together again.'))  # Output: 5
