def get_second_word(input_phrase):
    words = input_phrase.split()
    return words[1]

# Input: 'Nancy FreeHafer', Output: 'FreeHafer'
# Input: 'Andrew Cencici', Output: 'Cencici'
# Input: 'Jan Kotas', Output: 'Kotas'
# Input: 'Mariya Sergienko', Output: 'Sergienko'
# Input: 'Launa Withers', Output: 'Withers'

# Test the function
print(get_second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(get_second_word('Andrew Cencici'))   # Output: Cencici
print(get_second_word('Jan Kotas'))        # Output: Kotas
print(get_second_word('Mariya Sergienko')) # Output: Sergienko
print(get_second_word('Launa Withers'))    # Output: Withers
