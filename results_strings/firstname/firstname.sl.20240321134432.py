# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'], Output: Nancy
# Input: ['Andrew Cencici'], Output: Andrew
# Input: ['Jan Kotas'], Output: Jan
# Input: ['Mariya Sergienko'], Output: Mariya

def first_word(input_phrase):
    return input_phrase[0].split()[0]

# Test cases
print(first_word(['Nancy FreeHafer']))  # Output: Nancy
print(first_word(['Andrew Cencici']))  # Output: Andrew
print(first_word(['Jan Kotas']))  # Output: Jan
print(first_word(['Mariya Sergienko']))  # Output: Mariya
