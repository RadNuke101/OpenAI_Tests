# Prompt: if inputted phrase has more than one word, return the first word, else return nothing
# Input: ['The quick brown fox.'], Output: The
# Input: ['quick brown fox.'], Output: quick
# Input: ['fox'], Output: 

def first_word(input_phrase):
    words = input_phrase.split()
    if len(words) > 1:
        return words[0]
    else:
        return ""

# Test cases
print(first_word('The quick brown fox.'))  # Output: The
print(first_word('quick brown fox.'))      # Output: quick
print(first_word('fox'))                    # Output: 
