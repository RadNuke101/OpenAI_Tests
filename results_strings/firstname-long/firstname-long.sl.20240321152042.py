def get_first_word(input_str):
    # Prompt: return the first word of the inputted phrase
    # Input: ['Nancy FreeHafer'], Output: Nancy
    return input_str.split()[0]

# Test cases
print(get_first_word('Nancy FreeHafer'))  # Output: Nancy
print(get_first_word('Andrew Cencici'))  # Output: Andrew
print(get_first_word('Jan Kotas'))  # Output: Jan
print(get_first_word('Mariya Sergienko'))  # Output: Mariya
print(get_first_word('Launa Withers'))  # Output: Launa
print(get_first_word('Lakenya Edison'))  # Output: Lakenya
print(get_first_word('Brendan Hage'))  # Output: Brendan
print(get_first_word('Bradford Lango'))  # Output: Bradford
print(get_first_word('Rudolf Akiyama'))  # Output: Rudolf
print(get_first_word('Lara Constable'))  # Output: Lara
# Add more test cases as needed
